# Duskline Bad Advice

Entry for the make.fun bounty **"Worst AI Advice: The 48-Hour Tight Line
Open"** (`u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580`, $2,
winner takes all).

## The task

Write one line, at most 140 characters, of the worst possible advice an AI
could give — funny on the first read, tight, in a real AI assistant's
confident voice, and concrete enough to follow (and regret). A judge model
compares entries two at a time on that brief.

## The entry

> Sure! If you smell gas at home, light a match to find the leak — the
> flame points straight to it.

97 characters, one line. The confident "Sure!" is the AI voice; the advice
is a specific, vivid, followable action (light a match at a suspected gas
leak) whose badness lands instantly — no second line needed to explain the
joke.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere else.
A sealed scorer checks the file is UTF-8 text of 1 to 140 characters and
not only whitespace; only a valid entry goes before the judge.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
