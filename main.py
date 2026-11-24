#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes a single fortune line for the houseplant on the windowsill
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
"""

import os
import sys

FORTUNE = (
    "Tomorrow's sunbeam has booked your favourite leaf, "
    "and by week's end you'll be the proudest green thing on this sill."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    line = FORTUNE.strip()

    # Runtime self-check: exactly one non-blank line, 1-120 chars (UTF-8).
    if not line:
        print("error: fortune line is empty", file=sys.stderr)
        return 1
    # Reject blank or whitespace-only content as well as embedded newlines.
    if not line.strip():
        print("error: fortune line is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: fortune must be exactly one line", file=sys.stderr)
        return 1
    char_count = len(line)
    if char_count > 120:
        print(
            f"error: fortune is {char_count} chars, over the 120-char limit",
            file=sys.stderr,
        )
        return 1
    if len(line.encode("utf-8")) > 120 * 4:
        print("error: fortune too long in UTF-8 bytes", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Round-trip check: what landed on disk must be exactly the one line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("error: entry.txt on disk does not match the fortune", file=sys.stderr)
        return 1

    print(f"wrote entry.txt ({char_count} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
