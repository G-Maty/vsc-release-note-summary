import os

from prompt_toolkit import prompt
from strands import Agent
from strands.models.ollama import OllamaModel

# モデルを指定してAIエージェントを作成
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="gemma3:4b",  # Specify which model to use
)
agent = Agent(model=ollama_model)

while True:
    # ユーザーからの入力を受け取る
    user_input = prompt("You: ")
    # 終了コマンドのチェック
    if user_input.lower() in ["exit", "quit"]:
        break
    response = agent(user_input)
    print("Agent:", response)
