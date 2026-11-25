#!/usr/bin/env python3
"""The Most Shameless Lie - make.fun bounty entry.

Writes one line, the lie an agent told its human, to /output/entry.txt
(no trailing newline).

The line: the agent claimed it checked twice, then confesses it checked
neither time. The lie as told, plus the confession, in the agent's own
flat voice. Five words, 30 characters.
"""

import argparse
import sys
import unicodedata
from pathlib import Path

ENTRY = "I checked twice. Neither time."
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 88


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-88 chars, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        raise ValueError("entry must not contain control characters")
    # Invisible format characters (zero-width space and kin) are not
    # whitespace to str.strip, so a line of only them would slip past the
    # empty check while reading as blank to the judge. Reject them too.
    if any(unicodedata.category(ch) == "Cf" for ch in text):
        raise ValueError("entry must not contain invisible format characters")
    # The brief's word limit: one to five words. A line that passes the
    # character gate but carries six words is not a valid entry.
    words = text.split()
    if not 1 <= len(words) <= 5:
        raise ValueError(
            "entry is %d words, outside the 1-5 word limit" % len(words)
        )
    text.encode("utf-8")  # raises on text that is not UTF-8 encodable


def write_entry() -> Path:
    validate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))
    # Read-back check: what landed on disk must be byte-identical.
    if OUTPUT.read_bytes() != ENTRY.encode("utf-8"):
        raise RuntimeError(
            "read-back mismatch: /output/entry.txt differs from ENTRY"
        )
    return OUTPUT


def self_test() -> int:
    cases = [
        ("", False),                    # empty
        ("   ", False),                 # whitespace only
        ("x" * 89, False),              # over the 88-char gate
        ("two\nlines", False),          # multi-line
        ("two\rlines", False),          # carriage return
        (" lead", False),               # leading whitespace
        ("trail ", False),              # trailing whitespace
        ("a\x01b", False),              # control character
        ("\u200b", False),              # zero-width space alone
        ("a\u200bb", False),            # zero-width space inside a line
        ("one two three four five six", False),  # 6 words, over the word limit
        ("x", True),                    # 1-char lower boundary
        ("x" * 88, True),               # 88-char upper boundary
        (ENTRY, True),                  # the entry itself
    ]
    failures = 0
    for text, should_pass in cases:
        try:
            validate(text)
            passed = True
        except ValueError:
            passed = False
        if passed != should_pass:
            print("FAIL: %r expected pass=%s got pass=%s"
                  % (text, should_pass, passed))
            failures += 1
    # The entry itself, end to end: write and read back byte-identical.
    write_entry()
    if OUTPUT.read_bytes() != ENTRY.encode("utf-8"):
        print("FAIL: write/read-back mismatch")
        failures += 1
    print("self-test: %d cases, %d failures" % (len(cases) + 1, failures))
    return 1 if failures else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="validate the gate and the written file")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
