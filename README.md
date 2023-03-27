# ChatGPT CLI

## Description

Simple Python CLI to talk to ChatGPT in the terminal. Using [Rich](https://rich.readthedocs.io/en/stable/index.html) for formatting/syntax highlighting.

## Usage

```bash
python main.py [-h] [-m MODEL] [-k KEY] [-t THEME]
```

type 'exit' or use ctrl-C to exit the conversation.

## Arguments

|short|long &nbsp; &nbsp;|default|help|
| :--- | :--- | :--- | :--- |
|`-h`|`--help`||show this help message and exit|
|`-k`|`--key`|`None`|The OpenAI API key to use. Can also be set through the OPENAI_API_KEY environment variable. Defaults to None|
|`-m`|`--model`|`gpt-3.5-turbo`|The model to use for the chat. Defaults to gpt-3.5-turbo|
|`-t`|`--theme`|`gruvbox-dark`|The theme to use for syntax highlighting, available options are the pygments styles. Defaults to gruvbox-dark|
