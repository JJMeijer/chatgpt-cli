from chat_gpt import ChatGPT
from chat_gpt.arguments import parser


def main(key, model, theme):
    """Main function"""
    ChatGPT(key, model, theme)


if __name__ == "__main__":
    args = parser.parse_args()
    main(
        key=args.key,
        model=args.model,
        theme=args.theme,
    )
