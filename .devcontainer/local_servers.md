claude mcp add ado -s local .vscode/local_servers/ado-server.js
claude mcp add context7 -s local .vscode/local_servers/context7-server.js
claude mcp add desktop-commander -s local .vscode/local_servers/desktop-commander-server.js
claude mcp add filesystem-server -s local .vscode/local_servers/filesystem-server.js
claude mcp add memory-server -s local .vscode/local_servers/memory-server.js
claude mcp add sequential-thinking -s local .vscode/local_servers/sequential-thinking-server.js
claude mcp add --transport http Ref https://api.ref.tools/mcp\?apiKey\=ref-40e54e07e3ea2a7f36b9
claude mcp add semgrep uvx semgrep-mcp
claude mcp add exa -e EXA_API_KEY=e72b1a0c-0764-41bc-b2ba-5647cb81d582 -- npx -y exa-mcp-server