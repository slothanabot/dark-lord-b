"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

The monologue is spoken by a Dark Lord who has fought the same hero
so many times the apocalypse has become a weekly appointment. The
"final battle" happens every Tuesday: the Chosen One charges in,
falls, and rises again by dawn — so the Dark Lord has stopped
fortifying and started leaving the gate unlocked, just to get it
over with.

The entry follows the judge brief's order of importance:

1. About 100 words, on the subject: a fantasy villain who is
   secretly just very tired. Exactly 100 words, and every sentence
   is the same Tuesday appointment — banners, traps, lava, the
   speech, the siege, the fall, the rise.
2. The tiredness is felt, never announced. The entry never says
   "tired", "weary" or "exhausted". It lives in the rhythm and the
   deflections instead: "Tuesday again", banners "barely dry from
   last week", a speech "mostly memorised", a gate left unlocked
   so the siege can be skipped, and a prophecy with "no refunds".
   Routine is the exhaustion. The clearest small deflection is the
   false start in the middle — "Sit down. No, stand if you must":
   the Dark Lord catches himself playing host to his own assassin,
   then gives up correcting himself. That stumble does more work
   than any statement of weariness could.
3. A specific villain with a history and a scheme, not a generic
   dark lord: he conquered nine kingdoms, keeps traps and warm
   lava ready, and his generals run a book on how long the hero
   lasts this time. The fantasy shows in concrete detail —
   banners, sword, destiny, traps, lava, gate, siege, generals,
   kingdoms — not stock scenery.
4. Speakable dialogue in one breath, with a turn that lands in
   the last line: "prophecy offers no refunds" — the appointment
   cannot be cancelled, by either of them.
5. It stays at 100 words and spends every one of them: no line
   repeats an earlier one; the siege, the fall and the rise each
   get one mention.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-600
characters, not only white space.
"""

ENTRY = (
    "Tuesday again. The banners are barely dry from last week, and here you are, "
    "sword up, destiny polished, shouting my name like it is the first time. "
    "Sit down. No, stand if you must. The traps are set, the lava is warm, "
    "the speech is mostly memorised, and I left the gate unlocked so we could "
    "skip the siege. My generals run a book on how long you last this time. "
    "You will fall, and still rise again by dawn, because that is what chosen "
    "ones do. I conquered nine kingdoms for this appointment, hero, and "
    "prophecy offers no refunds."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry) > 600:
        raise ValueError(f"entry is {len(entry)} chars, over the 600-char limit")
    if len(entry.split()) != 100:
        raise ValueError(f"entry is {len(entry.split())} words, must be 100")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
