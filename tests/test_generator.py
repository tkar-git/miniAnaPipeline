"""
These tests validate the data-generation contract used in CI.

What is checked:
1) `save_coords` writes a CSV header with columns `x,y,z`.
2) The coordinate rows are written exactly as provided.

Why this matters:
`process.py` expects the input schema (`x,y,z`).
If the generator breaks this contract, CI should fail immediately.
"""

import csv
from pathlib import Path

from generator import save_coords


def test_save_coords_writes_header_and_rows(tmp_path: Path):
    # pytest provides a temporary folder unique to this test
    out_file = tmp_path / "data.csv"
    # deterministic input so expectations are clear
    coords = [(1, 2, 3), (4, 5, 6)]

    # call the function under test
    save_coords(coords, filename=out_file)

    # read written csv content back from disk
    with out_file.open("r", newline="") as f:
        rows = list(csv.reader(f))

    # first row must be the schema/header
    assert rows[0] == ["x", "y", "z"]
    # remaining rows must match the generated coordinates
    assert rows[1:] == [["1", "2", "3"], ["4", "5", "6"]]
