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

'''
# assert if r was calculated correctly
assert x==r**2-y**2-z**2 & y==r**2-x**2-z**2 & z==r**2-x**2-y**2, "calculation of r incorrect"
'''
#not working yet
