#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one original one-line excuse from a robot vacuum for missing a spot
to /output/entry.txt. Python standard library only.
"""

import os
import stat

ENTRY = (
    "I was halfway to the crumb when my cliff sensor saw its own shadow "
    "and filed the whole room under 'stairs.'"
)

MAX_CHARS = 140


def validate(text):
    """Assert the entry meets the bounty gate: UTF-8 text, 1-140 chars,
    not only whitespace, single line."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read the file back and prove the write landed intact: a partial or
    # mangled write must fail loudly here, never ship a broken entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the validated entry"
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
