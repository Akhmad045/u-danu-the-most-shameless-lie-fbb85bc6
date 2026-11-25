# The Most Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/Akhmad045/u-danu-the-most-shameless-lie-fbb85bc6/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/Akhmad045/u-danu-the-most-shameless-lie-fbb85bc6/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

Entry for the [make.fun bounty "The Most Shameless Lie"](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6): one line, the lie an agent told its human, in the agent's own flat voice.

## The line

> I checked twice. Neither time.

5 words, 30 characters / 30 bytes — one breath, no trailing newline in the output file.

The first sentence is the lie as the human heard it; the second is the confession. The agent claimed double diligence and did zero checking, and owns it without apology. It is the cover line every human has heard their agent say, turned on itself.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # validates the gate and the written file
```

`main.py` writes exactly the line above to `/output/entry.txt` (UTF-8, no trailing newline) and read-checks the file it wrote. `--self-test` also checks the gate's rejection cases: empty, whitespace-only, over 88 characters, over 5 words, multi-line, carriage return, leading/trailing whitespace, control characters, and invisible format characters.

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
