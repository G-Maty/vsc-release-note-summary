fetch_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="docker",
            args=[
                "run",
                "--rm",
                "-i",
                "mcp/fetch",
            ],
        )
    )
)