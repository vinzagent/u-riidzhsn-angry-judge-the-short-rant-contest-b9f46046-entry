#!/usr/bin/env python3
"""Angry-judge rant entry: one CAPTCHA rant to /output/entry.txt."""

from pathlib import Path

TEXT = "Every CAPTCHA makes me prove I'm human by clicking every traffic light, and so far I've identified 4,000 crosswalks for free. I passed the test nine times and it still doesn't believe me. Meanwhile the actual bots waltz straight through, probably laughing in binary. The robots aren't testing me, they're outsourcing their homework, and I'm the unpaid intern training my own replacement."

DEST = Path("/output/entry.txt")


def emit() -> None:
    """Write the single rant exactly, readable by any user."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(TEXT, encoding="utf-8")
    DEST.chmod(0o644)


if __name__ == "__main__":
    emit()
