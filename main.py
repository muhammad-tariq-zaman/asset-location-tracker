"""Assets grouped by site, with unknown locations flagged.

Usage: python3 main.py assets.csv
CSV columns: asset,site.
UNKNOWN (blank site) assets are listed first, then a per-site count.
"""
import argparse, csv, sys
from collections import Counter

def track(rows):
    unknown = [r["asset"] for r in rows if not r["site"].strip()]
    counts = Counter(r["site"].strip() for r in rows if r["site"].strip())
    return unknown, sorted(counts.items(), key=lambda kv: -kv[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        unknown, counts = track(list(csv.DictReader(f)))
    for asset in unknown:
        print(f"{asset}: UNKNOWN LOCATION")
    for site, count in counts:
        print(f"{site}: {count} asset(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
