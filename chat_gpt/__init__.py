import os

import openai

from .constants import ASSISTANT, SYSTEM, SYSTEM_MESSAGE, USER
from .console import console
from .printer import Printer
from .exit_app import exit_app


class ChatGPT:
    def __init__(self, key, model, theme) -> None:
        console.clear()

        api_key = key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            console.print(
                "[bold yellow]No API key was given through the --key argument or through the OPENAI_API_KEY environment variable.\n"
            )

            exit_app()

        openai.api_key = api_key

        self.model = model
        self.theme = theme

        self.messages = [{"role": SYSTEM, "content": SYSTEM_MESSAGE}]

        self.run()

    def add_message(self, role: str, content: str) -> None:
        """Adds a message to the messages list"""
        self.messages.append({"role": role, "content": content})

    def get_response(self) -> None:
        """Gets a response from openai chat completion stream"""
        full_message = ""

        console.line()
        console.rule("[bold green4]ChatGPT")

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            stream=True,
        )

        printer = Printer(self.theme)

        for chunk in response:
            text = chunk["choices"][0]["delta"].get("content", "")
            full_message += text

            printer.add(text)

        console.print("\n\n")

        self.add_message(ASSISTANT, full_message)
        self.user_prompt()

    def user_prompt(self) -> None:
        """Prompts the user for input"""
        user_input = console.input(
            console.rule("[bold dark_turquoise]User"),
        )

        if user_input == "exit":
            exit_app()

        console.line()
        self.add_message(USER, user_input)
        self.get_response()

    def run(self) -> None:
        """Start the App"""
        self.user_prompt()
