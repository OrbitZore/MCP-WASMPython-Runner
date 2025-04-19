from mcp.server.fastmcp import FastMCP, Context
from sys import version as python_formatted_version
import tempfile
import aiofiles
from os import path,environ
import asyncio
APP_NAME = "MCP-WASMPython"
mcp = FastMCP(APP_NAME)

@mcp.tool()
async def RunPython运行Python(code: str) -> str:
    """Run Python Code(limited in 10s,with 1kb output),运行Python代码（最长运行10s，最大1kb输出大小）
    """
    with tempfile.TemporaryDirectory('mcp-py') as temp_dir:
        filename = path.join(temp_dir, 'a.py')
        async with aiofiles.open(filename, mode='w') as file:
            await file.write(code)
        
        proc = await asyncio.create_subprocess_exec('wasmer', 'run',
                                            '--mapdir', f"/prog:{temp_dir}",
                                            "-q", "--no-tty",
                                            "python/python", "--", "-q", "/prog/a.py", stdin=None, stdout=asyncio.subprocess.PIPE)
        try:
            result,_ = await asyncio.wait_for(proc.communicate(), timeout=10)
            return result.decode()[:1024:]
        except TimeoutError:
            proc.terminate()
            return "TimeoutError"

mcp.settings.host = environ.get(APP_NAME+"_HOST",'0.0.0.0')
mcp.settings.port = int(environ.get(APP_NAME+"_PORT",'8000'))
asyncio.run(mcp.run_sse_async())