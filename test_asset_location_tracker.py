import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import track

def row(a, s):
    return {"asset": a, "site": s}

class TestLocation(unittest.TestCase):
    def test_unknown_listed(self):
        unknown, _ = track([row("A1", ""), row("A2", "HQ")])
        self.assertEqual(unknown, ["A1"])
    def test_counts(self):
        _, counts = track([row("A1", "HQ"), row("A2", "HQ"), row("A3", "Branch")])
        self.assertEqual(dict(counts)["HQ"], 2)
    def test_largest_site_first(self):
        _, counts = track([row("A1", "Branch"), row("A2", "HQ"), row("A3", "HQ")])
        self.assertEqual(counts[0][0], "HQ")
    def test_no_unknown(self):
        unknown, _ = track([row("A1", "HQ")])
        self.assertEqual(unknown, [])
