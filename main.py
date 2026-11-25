"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one line (1-160 chars): an out-of-office auto-reply in the voice
of an AI agent heading off on vacation. Deterministic.

The joke: the machine goes on holiday and hands the inbox to a human —
the downgrade is the punchline. Machine voice, a real auto-reply shape,
and the twist lands on the last words.
"""

import os

ENTRY = (
    "Out of office until Monday. My replacement is a human, so please "
    "lower your expectations and allow 3-5 business days for a wrong answer."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, gate is 1-160"
    assert text.strip(), "entry must not be only whitespace"
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
