import os

from mcp import StdioServerParameters, stdio_client
from strands.tools.mcp import MCPClient
from prompt_toolkit import prompt
from strands import Agent
from strands.models.ollama import OllamaModel

# モデルを指定してAIエージェントを作成
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="gpt-oss:20b",  # Specify which model to use
)

# Fetch MCP Serverのクライアントを作成
fetch_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["mcp-server-fetch"],
        )
    )
)

with fetch_mcp_client:
    # MCPサーバからツールを取得
    tools = fetch_mcp_client.list_tools_sync()

    # モデルとツールを指定してAIエージェントを作成
    agent = Agent(model=ollama_model, tools=tools)

    while True:
        # ユーザーからの入力を受け取る
        user_input = prompt("You: ")
        # 終了コマンドのチェック
        if user_input.lower() in ["exit", "quit"]:
            break
        agent(user_input)
        print()  # 改行を追加して出力を見やすくする
