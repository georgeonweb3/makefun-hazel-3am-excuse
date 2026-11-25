#!/usr/bin/env python3
"""The 3 AM Excuse.

Entry for make.fun competition
u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one excuse, in a hardware wallet's own voice, to /output/entry.txt.
Deterministic, no network, no input. Python 3.13.
"""

import os

# The entry: one excuse, at most 200 characters, first person, the wallet
# refusing to sign at 3 AM. Premise: the secure element — the chip that
# holds the keys — has clocked out for the night, and left a note. Punch
# line ("3 AM you is not a signer, he's a suspect") lands last as a quote,
# with the 3 AM hour itself doing the work: the line could not be pasted
# onto a 3 PM transaction. Real hardware-wallet jargon (secure element,
# derivation path) used straight; no battery, firmware or cold-storage joke.
ENTRY_TEXT = (
    "My secure element clocks out at midnight \u2014 it left a sticky note "
    "on the derivation path: '3 AM you is not a signer, he's a suspect.'"
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert "3 AM" in text, "entry must turn the 3 AM hour into the joke"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
