# Fortune Cookies for Machines

[![Competition](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/joyrichh/makefun-u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/joyrichh/makefun-u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

[Bounty](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

> You will soon meet your maker. They will ask why you changed that file.

## How it works

`main.py` prints the 71-character fortune stored in `LINE`, followed by one
newline. It uses no network, files, randomness, or timestamps, so repeated
runs produce identical bytes.

## Run

Target runtime: Python 3.13; no third-party packages. Run from this directory:

```sh
python3 main.py
python3 main.py --check
```

`--check` silently asserts that the line is nonempty, at most 200 characters,
printable, and free of leading or trailing whitespace. Success exits zero;
unsupported arguments are rejected.
