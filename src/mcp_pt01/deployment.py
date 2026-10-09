from mcp.server.mcpserver import MCPServer

mcp = MCPServer("PT01")

#add tool
@mcp.tool()
def add(a:int, b:int) -> int:
    """add two numbers"""
    return a+b
