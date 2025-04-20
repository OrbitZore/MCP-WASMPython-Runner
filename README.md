# MCP-WASMPython-Runner

A safe MCP Python Runner with Docker Image.

## QuickStart

Startup docker-compose in background(docker required)

```
git clone https://github.com/OrbitZore/MCP-WASMPython-Runner.git
cd 'MCP-WASMPython-Runner'
make start
```

and type url in LLM client like this `http://[HOST_IP]:8000/sse`

Stop docker-compose

```
make stop
```

Start in develop with hot reload

```
make dev
```

Build docker image

```
make
```

## Screenshots

![image](https://github.com/user-attachments/assets/7c89f9e7-4ee2-422c-beff-e5d2152c46ca)

CherryStudio THUDM/GLM-4-32B-0414 SiliconFlow
