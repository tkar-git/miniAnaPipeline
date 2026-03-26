import os.path
from os import path
import csv

# assert file exists
assert path.exists("data.csv"), "data.csv file does not exist"

# open and read CSV
with open("data.csv", newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # first row

    # check header
    assert header == ['x', 'y', 'z'], "header is not accurate"
