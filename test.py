from claude_code_sdk import query, ClaudeCodeOptions, AssistantMessage, TextBlock
import asyncio
# Simple query
# With options
options = ClaudeCodeOptions(
    allowed_tools=["Read", "Write", "Bash", "MCP"],  # Add MCP tool
    permission_mode='acceptEdits')


# prompt_message = '''Analyse the .devcontainer/requirements.txt and retrieve the python packages in that file. 
# Make a plan to use the context7 MCP to search for the python packages relevant documentation and code samples. 
# Then add all relevant documentation and all code samples to a .md file that will assist claude code. 
# Create a documentation package for each of them in the .claude/package_docs directory.'''
prompt_message = '''Analyse the .devcontainer/requirements.txt and retrieve the python packages in that file. 
Make a plan to use the Ref MCP to search for the python packages relevant documentation and code samples. 
Then add all relevant documentation and all code samples to a .md file that will assist claude code. 
Create a documentation package for each of them in the .claude/package_docs directory.'''



async def main():
    async for message in query(prompt=prompt_message, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)

if __name__ == "__main__":
    asyncio.run(main())