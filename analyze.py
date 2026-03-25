import csv
import numpy as np
import matplotlib.pyplot as plt

def analyze_data(file_path):
    radius = []
    theta = []
    phi = []

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            radius.append(float(row[0]))
            theta.append(float(row[1]))
            phi.append(float(row[2]))

        
  

