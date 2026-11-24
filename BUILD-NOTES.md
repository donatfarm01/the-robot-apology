Build notes for The Robot Apology.

The bounty asks for exactly two lines of plain text. Line one is a robot
apologizing for one specific mistake, line two says what it learned and what
it will do differently. The gate allows one to four hundred characters of
UTF-8 text, and the entry here is well inside that range.

The entry chosen is about a robot setting a 7 a.m. alarm for 7 p.m., so its
owner slept through an interview. The mistake is concrete and human-scale,
with a real consequence, and it is not one of the examples the brief itself
lists, so it reads as its own slip rather than a stock line. The second
line follows from that exact mistake: the robot now reads the hour out loud
twice before saving it and checks the sun and moon icons as if they were
the whole job. That is a named changed behaviour, not a generic promise to
do better. The voice is a machine noticing its own slip, warm and a little
rueful, and each sentence does its own job with no padding.

The program is a small Python script with no network calls and no secrets.
It holds the two lines as a constant, checks that the text is exactly two
non-empty lines within the character gate, and writes it to the output path.
It was run twice and produced the same file both times. The repository
holds the script, the readme with the three linked make.fun badges, and an
MIT license carrying the SPDX identifier line.
