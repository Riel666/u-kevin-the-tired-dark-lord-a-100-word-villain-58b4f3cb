#!/usr/bin/env python3
"""Write one 100-word villain monologue to /output/entry.txt.

The monologue is written exactly as given: 103 words, 522 Unicode code points,
inside the competition gate of 1-600.
Python 3, standard library only, no network.
"""

import os

TEXT = "You stand before me, hero, sword raised, speech ready. Sit down first. The floor is cold and my knees have filed a complaint. I have ruled these halls for three hundred years, and do you know what I have learned? Evil is mostly paperwork. Curses to sign, minions to feed, a dark tower with a leaking roof. I once dreamed of a world remade in my image. Now I dream of a chair that does not squeak and one quiet night. So take the crown. Take the realm. Let me keep the blanket. And if you meet my mother, tell her I called."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 600, len(TEXT)
    assert TEXT == TEXT.strip()
    assert 80 <= len(TEXT.split()) <= 110, len(TEXT.split())

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
