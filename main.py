#!/usr/bin/env python3
"""Angry-judge rant entry: one CAPTCHA rant to /output/entry.txt.

The rant is held as ordered beats and joined at runtime, then written
out with plain file IO so the deliverable is byte-exact.
"""

import os

OUT_PATH = os.path.join("/output", "entry.txt")


def rant_beats():
    """Ordered beats of the rant, in the order they are spoken."""
    return [
        "Every CAPTCHA makes me prove I'm human by clicking every "
        "traffic light, and so far I've identified 4,000 crosswalks for free.",
        "I passed the test nine times and it still doesn't believe me.",
        "Meanwhile the actual bots waltz straight through, probably "
        "laughing in binary.",
        "The robots aren't testing me, they're outsourcing their homework, "
        "and I'm the unpaid intern training my own replacement.",
    ]


def build_rant() -> str:
    """Join the beats into the single rant paragraph."""
    return " ".join(rant_beats())


def save(text: str, path: str = OUT_PATH) -> None:
    """Write the rant exactly and make it readable by any user."""
    if not text.strip():
        raise ValueError("rant must not be empty")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as out:
        out.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    save(build_rant())
