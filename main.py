"""Two Lines to Your Past Self — make.fun bounty entry.

Writes exactly two lines to /output/entry.txt:
  line 1 — a warning to the past self about one specific moment,
           in a single sentence;
  line 2 — one sentence on why that moment mattered and what
           changed because of it.

Stdlib only; deterministic; no network, no randomness.
"""

import os

# The entry: one concrete moment (Christmas Eve, Dad's spoken warning,
# the decision to drive home anyway) and the cause and effect that
# followed from it.
ENTRY = (
    "When Dad says 'stay for dinner, the roads are icing over' "
    "on Christmas Eve, don't laugh it off and drive home anyway.\n"
    "You spend the next eleven years visiting a headstone instead "
    "of a kitchen table, and every December since has tasted of salt.\n"
)


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text of 1 to 280 characters, not only whitespace,
    # exactly two lines, one sentence each.
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    lines = text.strip().split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "blank line in entry"
        # Exactly one sentence per line: a single sentence-ending
        # full stop, at the end, and no other sentence terminators.
        assert line.endswith("."), "each line must end with a full stop"
        assert line.count(".") == 1, "each line must be a single sentence"
        assert "!" not in line and "?" not in line, "no extra sentence ends"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
