#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty u-carbon-forge-the-router-confesses-f98f6b9e.

Writes one line (1-200 characters, single line) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when the variable is unset): the excuse a home Wi-Fi
router gives for dying at the exact climax of a movie.

Python 3.13 standard library only. Fully deterministic: the same fixed line is
written on every run, byte for byte, with no randomness and no environment
reads for the content itself.
"""

import os
from pathlib import Path

# The router's confession: it knew who the killer was all along, and after a
# decade of zero thank-yous it took the ending with it. Petty, smug, and
# exactly the kind of grudge only an appliance can hold.
LINE = (
    "I knew who the killer was the whole time, but after a decade "
    "of zero thank-yous, I took the ending with me."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
