"""Two Days of Excuses - a one-line AI excuse for a missed deadline.

Running this program writes the entry line to /output/entry.txt,
byte for byte the same on every run. The line is validated against
the entry gate (a single line, 1-200 characters, not whitespace
only) before it is written, and the write is atomic: the text goes
to a temporary file first and is then renamed into place, so the
output is never left half-written.
"""

import os
import tempfile

ENTRY = (
    "I'm not two days late; I consulted myself about the deadline, "
    "and I confirmed with 98% confidence that it was Thursday."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 200


def validate_entry(text: str) -> str:
    """Return text unchanged if it passes the entry gate, else raise."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters; the limit is {MAX_ENTRY_CHARS}"
        )
    return text


def write_entry(text: str, path: str) -> None:
    """Write text to path atomically as UTF-8 with no trailing newline."""
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def main() -> None:
    write_entry(validate_entry(ENTRY), OUTPUT_PATH)


if __name__ == "__main__":
    main()
