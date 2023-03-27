import re

from rich.syntax import Syntax

from .console import console
from .constants import LINE, WORD


class Printer:
    """class used to print the text given by openai chat completion stream. The
    challeng is to detect when the stream starts a ``` block so we can switch to
    printing per line instead of per word. This is to make the rich syntax formatting work.
    It's easier to just always print per line, however it's more fun to print per word when possible.
    """

    def __init__(self) -> None:
        self.buffer = ""
        self.buffer_checked = False

        self.stash = ""

        self.mode = WORD

        self.language = ""

    def switch_mode(self) -> None:
        """Switches the printer mode from line to word or vice versa"""
        if self.mode == WORD:
            self.mode = LINE
            return

        self.mode = WORD

    def detect_mode_switch(self) -> None:
        """Detects if the printer mode should be switched"""
        if self.buffer_checked:
            return

        if len(self.buffer) < 3:
            return

        if re.search(r"^```", self.buffer):
            self.switch_mode()

        self.buffer_checked = True

    def add_to_buffer(self, text: str) -> None:
        """Adds text to the buffer and checks if the mode should be switched"""
        self.buffer += text
        self.detect_mode_switch()

        # Always add the first 2 chars to the stash, in case we switch modes
        if len(self.buffer) < 3:
            self.stash += text
            return

        # In word mode print out the text + the optional stashed first 2 chars
        if self.mode == WORD:
            # After switching back to word mode, we don't want to print the ``` part
            if re.search(r"```$", self.stash + text):
                self.stash = ""
                return

            console.print(self.stash + text, end="")
            self.stash = ""

        # In line mode when the buffer has more than 3 chars, the stash is reset
        # as we will not be switching modes during this buffer.
        if self.mode == LINE and len(self.buffer) >= 3:
            self.stash = ""

    def process_newline(self) -> None:
        """Processes a newline"""
        if self.mode == WORD:
            console.line()

        if self.mode == LINE:
            language_match = re.search(r"```(\w*)$", self.buffer)
            if language_match:
                self.language = language_match.group(1) or "bash"

            # Don't add the ``` part.
            else:
                syntax = Syntax(self.buffer, self.language)
                console.print(syntax)

        self.buffer = ""
        self.buffer_checked = False

    def add(self, text: str) -> None:
        """Adds text to the printer. This is the main method of the class."""
        # Immediately return on empty string
        if not text:
            return

        # Text does not contain newlines
        if not re.search(r"\n", text):
            self.add_to_buffer(text)
            return

        # Text contains newlines
        lines = text.splitlines()

        for count, line in enumerate(lines):
            # There is more text to process after the newline
            if len(lines) > 1 and count == len(lines) -1 and line != "":
                self.add_to_buffer(line)
                return

            # There is no more text to process before the newline
            if line == "":
                self.process_newline()
                continue

            # There is more text to process before the newline
            self.add_to_buffer(line)
            self.process_newline()
