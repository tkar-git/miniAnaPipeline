import os.path
from os import path
import csv

# asserts if required data.csv file exists
assert path.exists("data.csv"), "data.csv file does not exists"

'''
#opens data.csv if exists and reads out rows with csv.reader
file = open(path.exists("data.csv"), newline='')
reader=csv.reader(file)
header=next(reader) #first line of csv file
assert header=='x,y,z', "header is not accurate"
'''
# doesnt work as intended yet
