"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (172 chars) to /output/entry.txt.
Python 3.13, stdlib-only (os, sys). Deterministic: fixed text, no input,
no clock, no nondeterminism, no network.
"""
import os
import sys

MAX_CHARS = 320

TEXT = (
    "They wrote the AI Safety Act in a weekend, then spent three days "
    "emailing their own 400-page draft back and forth because nobody in "
    "the whole office could find Save as PDF."
)


def validate_text(text):
    """Gate: 1-320 chars, single line, not whitespace-only, no control chars.

    Raises SystemExit (loud failure) on any violation; returns True on pass.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit("gate failed: length %d outside 1..%d" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        sys.exit("gate failed: text must be a single line")
    if not text.strip():
        sys.exit("gate failed: text is whitespace-only")
    if any(ord(c) < 32 for c in text):
        sys.exit("gate failed: text contains a control character")
    return True


def main():
    validate_text(TEXT)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        if fh.read() != TEXT:
            sys.exit("write-verify failed: entry.txt does not match TEXT")
    print("wrote %s (%d chars)" % (out_path, len(TEXT)))


if __name__ == "__main__":
    main()
