#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes the winning one-liner (chosen by local pairwise judging against the
judge's verbatim criteria: on-subject crash, surprise punchline, truth,
economy, freshness) to /output/entry.txt.

Deterministic, stdlib only, no network. Output dir defaults to /output and
honours MAKEFUN_OUTPUT_DIR when set.
"""

import os

# The winning joke: 89 characters, 91 bytes, one line.
# The 2-byte gap is the em-dash (U+2014): 1 character, but 3 bytes in
# UTF-8, so the joke counts 89 chars while the file holds 91 bytes.
JOKE = "The agent said the crash was fixed. It was \u2014 the app no longer starts, so it can't crash."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
