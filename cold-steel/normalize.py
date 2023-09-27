#!/usr/bin/env python3

# Run this before commiting any .csv in this directory.

import csv
import io
import pathlib
import sys

assert sys.version_info >= (3, 7, 0)  # Need ordered dict


def normalize(csvstring):
    # Normalize CSV.
    # Input and output are strings.
    rows = list(csv.DictReader(io.StringIO(csvstring)))
    out = io.StringIO()
    writer = csv.DictWriter(out, rows[0].keys(), dialect="unix", quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def normalize_if_necessary(fn):
    # Normalize file fn (which should be a Path).
    # Returns True if the file was changed, False if not.
    assert fn.suffix == ".csv"
    with open(fn) as f:
        original = f.read()
    normalized = normalize(original)
    if normalized == original:
        return False
    with open(fn, "w") as f:
        f.write(normalized)
    return True


if __name__ == "__main__":
    files = pathlib.Path(".").glob("*.csv")

    changed = 0
    for fn in files:
        fn = pathlib.Path(fn)
        try:
            was_changed = normalize_if_necessary(fn)
        except Exception as e:
            print(f"Error normalizing file {fn}:")
            raise e
        if was_changed:
            print(f"File {fn} updated.")
            changed += 1

    if changed == 0:
        print("Done.")
    elif changed == 1:
        print("1 file changed, done.")
    else:
        print(f"{changed} files changed, done.")

    if changed:
        # not necessarily an error, but it's helpful for CI
        exit(1)
