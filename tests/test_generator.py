from typing import List

import pytest
import analyze
import os

def test_create_coords():
    len = size
    lower_limit = 0
    upper_limit = 100
    coords = analyze.create_coords(cols=size, rand_lower=lower_limit, rand_upper=upper_limit)
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
    cords = [(1, 2, 3), (11, 12, 13)]
    filename = "test.csv"
    analyze.save_coords(cords, filename)
    assert os.path.exists(filename)

if __name__ == "__main__":
    pytest.main()

