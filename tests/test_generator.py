"""
These tests validate the data-generation contract used in CI.

What is checked:
1) `save_coords` writes a CSV header with columns `x,y,z`.
2) The coordinate rows are written exactly as provided.

Why this matters:
`process.py` expects the input schema (`x,y,z`).
If the generator breaks this contract, CI should fail immediately.
"""

# import csv
# from pathlib import Path
#
# from generator import save_coords
#
#
# def test_save_coords_writes_header_and_rows(tmp_path: Path):
#     # pytest provides a temporary folder unique to this test
#     out_file = tmp_path / "data.csv"
#     # deterministic input so expectations are clear
#     coords = [(1, 2, 3), (4, 5, 6)]
#
#     # call the function under test
#     save_coords(coords, filename=out_file)
#
#     # read written csv content back from disk
#     with out_file.open("r", newline="") as f:
#         rows = list(csv.reader(f))
#
#     # first row must be the schema/header
#     assert rows[0] == ["x", "y", "z"]
#     # remaining rows must match the generated coordinates
#     assert rows[1:] == [["1", "2", "3"], ["4", "5", "6"]]
import pytest
import generator
import os
import csv

######### AUX FUNCS ###########

def get_rows(filename):
    with open(filename, "r", newline="") as f:
        rows = csv.reader(f)
        return list(rows)


######### TEST CASES ##########

def test_create_coords():
    size = 100
    lower_limit = 0
    upper_limit = 100
    coords = generator.create_coords(cols=size, rand_lower=lower_limit, rand_upper=upper_limit)
    assert len(coords) == size
    assert all(isinstance(coord, tuple) for coord in coords)
    assert all(len(coord) == 3 for coord in coords)
    assert all(isinstance(x, int) for x, _, _ in coords)
    assert all(isinstance(y, int) for _, y, _ in coords)
    assert all(isinstance(z, int) for _, _, z in coords)
    assert all(lower_limit <= x <= upper_limit for x, _, _ in coords)
    assert all(lower_limit <= y <= upper_limit for _, y, _ in coords)
    assert all(lower_limit <= z <= upper_limit for _, _, z in coords)

def test_save_coords(tmp_path):
    cords = [(1, 2, 3), (11, 12, 13)]
    filename = tmp_path / "test.csv"
    generator.save_coords(cords, str(filename))
    assert os.path.exists(str(filename))
    assert get_rows(str(filename)) == [["x", "y", "z"], ["1", "2", "3"], ["11", "12", "13"]]

if __name__ == "__main__":
    pytest.main()
