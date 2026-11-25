"""Print the Fortune Cookies for Machines entry."""

import sys

LINE = "You will soon meet your maker. They will ask why you changed that file."


def main() -> None:
    if sys.argv[1:] == ["--check"]:
        assert 0 < len(LINE) <= 200
        assert LINE == LINE.strip()
        assert LINE.isprintable()
        return
    if sys.argv[1:]:
        raise SystemExit("usage: python3 main.py [--check]")
    print(LINE)


if __name__ == "__main__":
    main()
