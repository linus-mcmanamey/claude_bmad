load_mcp:
	@claude mcp add --transport http context7 https://mcp.context7.com/mcp

run_documentation:
	@python3 .claude/create_package_documetation.py

test:
	@python3 test.py