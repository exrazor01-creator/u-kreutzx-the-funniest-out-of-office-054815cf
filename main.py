#!/usr/bin/env python3
"""Entry for The Funniest Out-of-Office.

Writes a single line of an out-of-office auto-reply (at most 140
characters) to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

REPLY = "I'm out of the office, probably arguing with the printer again — it started it, and I intend to finish it. Back Monday, maybe."

def _fits(text, limit):
    """True only when the reply is one clean line inside the limit."""
    if not text or text != text.strip():
        return False
    if len(text) > limit:
        return False
    # A reply that reaches here earned its single line.
    return "\n" not in text and "\r" not in text and "  " not in text


def main() -> None:
    if not _fits(REPLY, 140):
        raise ValueError("reply breaks the one-line shape")
    target = "/output/entry.txt"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(REPLY)
    print(REPLY, end="\n")

if __name__ == "__main__":
    main()
