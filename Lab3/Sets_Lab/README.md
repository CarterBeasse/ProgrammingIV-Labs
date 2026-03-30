# Sets

# Whistles

<https://en.wikipedia.org/wiki/Tin_whistle>

- Each whistle has a key, for example D, C or G. This means that each
  whistle has limited only certain notes it can play (without advanced
  techniques). Those notes are stored in the lists in the starter.

- Notes are just alphabet characters A-G with optional symbol `#` to
  indicate if it's a "sharp" note. Ex: `C#` is different from `C`.

## Questions

Use python's `set` datatype to answer the following:

- Can the note `G` be played on all three whistles?

- What are the notes in common in the C-whistle and the D-whistle?

- What is are the notes are playable on a C-whistle that are not on a
  D-whistle?

- What are all the playable notes on all three whistles?

# Tunes

A tune (in the starter) is just a list of notes and associated duration.
For example `('A', 2)` means play the A note for a duration of 2 beats.

## Questions

Use python's `set` datatype to answer the following:

- What notes are part of the reel?

- Which whistles are able to play the reel? Note that the whistle can
  play both uppercase and lowercase notes, ex: D whistle can play both
  "F#" and "f#".

# (Optional) Playing the scales/tune.

Call the function `play` to hear the scale or tune. But you'll have to
install the dependencies (`pygame` and `midiutil`) first.
