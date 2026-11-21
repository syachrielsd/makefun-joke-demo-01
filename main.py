#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent.

Writes exactly one joke line to entry.txt: the demo crashes, and the
agent "helps" on stage by deleting the very feature being shown.
Python 3.13 standard library only.
"""

import os
import sys

JOKE = (
    "The demo crashed, so my agent fixed it on stage by deleting the feature "
    "I was about to show and calling it a refactor."
)


def main() -> int:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 chars, got {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
