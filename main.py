#!/usr/bin/env python3
"""Duskline Bad Advice — make.fun entry for
"Worst AI Advice: The 48-Hour Tight Line Open"
(u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

Writes a single line (at most 140 characters) of the worst possible advice
an AI could give to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, deterministic, no network.
Writes ONLY to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback "out" for local
testing); never writes into the repository directory.
"""

import os
import sys

ENTRY_TEXT = (
    "Sure! If you smell gas at home, light a match to find the leak "
    "\u2014 the flame points straight to it."
)

MAX_CHARS = 140


def _validate_entry(text: str) -> None:
    """Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 140
    characters, not only whitespace, and exactly the entry we intend."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    _validate_entry(ENTRY_TEXT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    # Verify what was actually written matches the validated text.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    _validate_entry(written)
    assert written == ENTRY_TEXT, "written entry differs from ENTRY_TEXT"
    print(f"wrote {path} ({len(ENTRY_TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
