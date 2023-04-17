#!/usr/bin/python3

# Copyright 2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/runish

"""Main runish script."""

import argparse
import unicodedata


def _show(char, name):
    """Show nicely a char and its name."""
    print(f"{char}  {name}")


def find(subseq):
    """Find a subsequence in all Unicode names."""
    subseq = subseq.upper()
    for i in range(0x1FFFF):
        try:
            name = unicodedata.name(chr(i))
        except ValueError:
            pass
        else:
            if subseq in name:
                _show(chr(i), name)


def explain(to_explain):
    """Explain a char or string showing its Unicode name(s)."""
    # support explaining strings
    if len(to_explain) > 1:
        for char in to_explain:
            explain(char)
        return

    name = unicodedata.name(to_explain)
    _show(to_explain, name)


def main():
    """Manage CLI interaction and call proper functionality."""
    parser = argparse.ArgumentParser()
    parser.add_argument("item", help="Item to find or explain.")
    parser.add_argument(
        "-f", "--find",
        help="Explicitly use the 'find' functionality.",
        action="store_const", dest="functionality", const="find")
    parser.add_argument(
        "-e", "--explain",
        help="Explicitly use the 'explain' functionality.",
        action="store_const", dest="functionality", const="explain")
    args = parser.parse_args()

    if args.functionality == "find":
        find(args.item)
    elif args.functionality == "explain":
        explain(args.item)
    else:
        if len(args.item) == 1:
            explain(args.item)
        else:
            find(args.item)


if __name__ == "__main__":
    main()
