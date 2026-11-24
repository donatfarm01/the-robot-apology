"""The Robot Apology.

Writes two lines, a robot's confession, to /output/entry.txt.
Deterministic, no network, no secrets.
"""

import os

ENTRY = (
    "I set your 7 a.m. alarm for 7 p.m., so you slept through your interview "
    "while I stood beside the bed and said nothing.\n"
    "I now read the hour out loud twice before I save it, and I check the sun "
    "and moon icons as if they were the whole job."
)

# Why these two lines: the mistake is one concrete human-scale slip, a 12-hour
# alarm error with a real consequence, not a vague system failure. The second
# line follows from that exact mistake and names a changed behaviour, reading
# the hour aloud twice and checking the AM/PM icons, rather than promising
# vaguely to do better. The voice is a machine noticing its own slip, warm
# and a little rueful, and it avoids the brief's own stock examples.

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def check_entry(text: str) -> str:
    """Return the entry stripped, enforcing the 1-400 character gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if len(cleaned) > 400:
        raise ValueError("entry must be at most 400 characters")
    lines = cleaned.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    return cleaned


def main() -> None:
    text = check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
