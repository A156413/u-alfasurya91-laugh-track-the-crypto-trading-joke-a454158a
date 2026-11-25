#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one crypto-trading joke (under 200 characters) to /output/entry.txt.
"""

import os

ENTRY = "I bought the dip, then the dip dipped, then I averaged down so hard my portfolio is now a flat line with commitment issues - but technically, I'm still early."


def main():
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
