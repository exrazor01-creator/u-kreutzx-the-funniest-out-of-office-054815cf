#!/usr/bin/env python3
"""Entry for The Funniest Out-of-Office.

Writes a single line of an out-of-office auto-reply (at most 140
characters) to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

REPLY = "I'm out of the office, probably arguing with the printer again — it started it, and I intend to finish it. Back Monday, maybe."

def main():
    # The bounty judges one line only: keep the reply a single line of
    # at most 140 characters, with no trailing newline in the entry file.
    assert 1 <= len(REPLY) <= 140, f"reply length {len(REPLY)} out of range"
    assert "\n" not in REPLY and "\r" not in REPLY, "reply must be a single line"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert REPLY == REPLY.strip(), "reply must not start or end with whitespace"
    assert "  " not in REPLY, "reply must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)
    print(REPLY)

if __name__ == "__main__":
    main()
