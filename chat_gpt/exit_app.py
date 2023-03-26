import sys
import signal

from chat_gpt.console import console


def exit_app():
    """Exits the app"""
    console.print("[bold red]Exiting...")
    sys.exit(0)


def signal_handler(_signal, _frame):
    """Handler to exit app on ctrl-c"""
    exit_app()


signal.signal(signal.SIGINT, signal_handler)
