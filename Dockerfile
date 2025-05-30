FROM archlinux:latest
# add python
RUN pacman -Syy --noconfirm python uv wasmer
# warm wasmer
RUN wasmer run -q --no-tty python/python -- -c "print(1+1)"
# copy sources
ADD ./mcp-wasmpython-runner /opt/mcp-wasmpython-runner
WORKDIR /opt/mcp-wasmpython-runner
# uv install
RUN uv sync
# expose port
EXPOSE 8000/tcp
EXPOSE 8000/udp
ENTRYPOINT ["/opt/mcp-wasmpython-runner/start.sh"]