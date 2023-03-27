from argparse import ArgumentParser

parser = ArgumentParser(
    prog="chatgpt",
    description="Terminal Interface for Chat GPT using rich package as the formatter",
)

parser.add_argument(
    "-k", "--key",
    action="store",
    default=None,
    dest="key",
    required=False,
    help="The OpenAI API key to use. Can also be set through the OPENAI_API_KEY environment variable. Defaults to None",
)

parser.add_argument(
    "-m", "--model",
    action="store",
    default="gpt-3.5-turbo",
    dest="model",
    required=False,
    help="The model to use for the chat. Defaults to gpt-3.5-turbo",
)

parser.add_argument(
    "-t", "--theme",
    action="store",
    default="gruvbox-dark",
    dest="theme",
    required=False,
    help="The theme to use for syntax highlighting, available options are the pygments styles. Defaults to gruvbox-dark",
)

args = parser.parse_args()
