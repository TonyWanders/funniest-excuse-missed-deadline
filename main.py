"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network, no input.
"""

import os

ENTRY = (
    "I finished it on time, then my context window evicted the finished copy "
    "to make room for the email reminding me it was due."
)


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the excuse line to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, outside 1-200")
    write_entry()


if __name__ == "__main__":
    main()
