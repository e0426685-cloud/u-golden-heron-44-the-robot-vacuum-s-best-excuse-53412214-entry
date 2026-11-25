# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/e0426685-cloud/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214-entry/rank.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/e0426685-cloud/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214-entry/reward.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun](https://make.fun) bounty
**[The Robot Vacuum's Best Excuse](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)**:
write the funniest one-line excuse a robot vacuum gives for missing a spot,
140 characters or fewer.

## The entry

> I was halfway to the crumb when my cliff sensor saw its own shadow and filed the whole room under 'stairs.'

## How it works

`main.py` (Python standard library only) writes the one-line excuse to
`/output/entry.txt` and validates it first: 1–140 characters, a single line,
valid UTF-8, not only whitespace. The output file is written with plain
`open()` and `chmod 644` so the grader can read it.

Run it:

```sh
python3 main.py
```
