"""Write the make.fun dad-joke entry to entry.txt.

The whole entry is one short text. It is written as UTF-8 with no trailing
newline, into MAKEFUN_OUTPUT_DIR when that is set, else /output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be 1..280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "entry.txt"
    data = text.encode("utf-8")
    with open(out_path, "wb") as handle:
        handle.write(data)

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
