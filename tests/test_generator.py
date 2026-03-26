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

def test_save_coords():
    coords = [(1, 2, 3), (11, 12, 13)]
    filename = "test.csv"
    generator.save_coords(coords, filename)
    assert os.path.exists(filename)
    assert get_rows(filename) == [["x", "y", "z"], ["1", "2", "3"], ["11", "12", "13"]]
    os.remove(filename)

if __name__ == "__main__":
    pytest.main()

