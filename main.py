import sys
import signal

from chat_gpt import ChatGPT


def main():
    chatGPT = ChatGPT()

def sigint_handler(signum, frame):
    print("\nExiting...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == '__main__':
    main()
