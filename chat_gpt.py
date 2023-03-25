from enum import Enum
import os

from rich.console import Console
import openai

from constants import ASSISTANT, SYSTEM, SYSTEM_MESSAGE, USER

openai.api_key = os.getenv("OPENAI_API_KEY")
console = Console()

class CodeBlockStatus(Enum):
    IDLE = 0
    STARTING = 1
    IN_PROGRESS = 2
    ENDING = 3

class ChatGPT:
    def __init__(self) -> None:
        console.clear()
        self.messages = [{"role": SYSTEM, "content": SYSTEM_MESSAGE}]

        self.run()

    def add_message(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})

    def get_response(self) -> None:
        full_message = ""

        console.line()
        console.rule("[bold green4]ChatGPT")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            stream=True,
        )

        for chunk in response:
            text = chunk["choices"][0]["delta"].get("content", "")
            full_message += text

            console.print(text, end="")

        console.line()

        self.add_message(ASSISTANT, full_message)
        self.user_prompt()

    def user_prompt(self) -> None:
        console.line()
        user_input = console.input(
            console.rule("[bold dark_turquoise]User"),
        )
        console.line()
        self.add_message(USER, user_input)
        self.get_response()

    def run(self) -> None:
        self.user_prompt()
