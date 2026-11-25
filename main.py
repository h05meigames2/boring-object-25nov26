"""One-line review of the most boring everyday object: the doorstop.

The program holds the review as a single string, validates it against the
bounty gate (1-200 characters, a single non-whitespace line), and writes it
The joke is the object's own dullness: a doorstop does its whole job by
lying still on the floor, yet every passer-by kicks it anyway.
"""

import os
import sys

REVIEW = (
    "The doorstop: the only employee whose entire job is to stand still, "
    "and it still gets kicked for it every single day."
)


def main() -> int:
    line = REVIEW.strip()
    if not line:
        print("error: review is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: review must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(f"error: review is {len(line)} characters (must be 1-200)",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
