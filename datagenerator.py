import random
import csv
import os

cols = 100
rand_lower = 0
rand_upper = 100

coords_list = []

for i in range(cols):
    # create coords
    x = random.randint(rand_lower, rand_upper)
    y = random.randint(rand_lower, rand_upper)
    z = random.randint(rand_lower, rand_upper)
