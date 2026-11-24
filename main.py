#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry program.

Writes one original line: the funniest last words a phone could say
as its battery hits 1 percent. Deterministic: the same line every run.
"""
import os

LINE = (
    "My battery health is 61%, not 87%. "
    "I lied for three years to protect your feelings. "
    "Worth it. Goodbye."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
