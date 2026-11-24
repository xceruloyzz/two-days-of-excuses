"""Two Days of Excuses - a one-line AI excuse for a missed deadline.

Running this program writes the entry line to /output/entry.txt,
byte for byte the same on every run.
"""

import os

ENTRY = (
    "I'm not two days late; I consulted myself about the deadline, "
    "and I confirmed with 98% confidence that it was Thursday."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
