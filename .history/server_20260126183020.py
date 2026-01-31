from mcp.server.fastmcp import FastMCP

mcp=FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "send a greeting "
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run("streamable-http")   

