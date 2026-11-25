#!/usr/bin/env python3
"""Entry program for the make.fun one-line bounty.

Writes the entry line to /output/entry.txt exactly as judged:
one line, no trailing newline. The OUTPUT_DIR environment variable
may redirect the output folder for local testing; the default is
/output, which is where the grader reads the entry.
"""

import os
from pathlib import Path

ENTRY_TEXT = "I finished your sentences. This one you finish alone."


def validate(text):
    """Return the entry as UTF-8 bytes after checking the gate."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must hold 1 to 200 characters")
    if "\n" in text:
        raise ValueError("entry text must stay on a single line")
    data = text.encode("utf-8")
    if len(data) != len(text):
        raise ValueError("entry text must stay pure ASCII")
    return data


def destination():
    """Resolve where entry.txt belongs for this run."""
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def write_entry():
    """Validate the line, then write its bytes with no newline."""
    destination().write_bytes(validate(ENTRY_TEXT))


def main():
    write_entry()


if __name__ == "__main__":
    main()
