# Fortune in a Pot

A single-line fortune for the houseplant on the windowsill — kind, funny,
and written for this plant in this window, not any plant anywhere.

[![Make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/aldy007x/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/aldy007x/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

## Entry

> Tomorrow's sunbeam has booked your favourite leaf, and by week's end you'll be the proudest green thing on this sill.

## How it works

`main.py` writes the fortune to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It is
deterministic, uses only the standard library, makes no network calls, and
self-checks that the entry is exactly one non-blank line of 1–120 characters
before writing it.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
