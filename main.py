#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- one haiku, written to /output/entry.txt."""

import os

HAIKU = """the log line stays silent
i scatter print lines like bread
the bug eats them all"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
        f.write("\n")


if __name__ == "__main__":
    main()
