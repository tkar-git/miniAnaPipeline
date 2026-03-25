import csv
import matplotlib.pyplot as plt
from pathlib import Path

def analyze_data():
    r, theta, phi = [], [], []

    file_path = Path(__file__).parent / "data.csv"

    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  #Header skip

        for row in reader:
            r.append(float(row[0]))
            theta.append(float(row[1]))
            phi.append(float(row[2]))

    plt.figure(figsize=(8, 5))
    plt.boxplot([r, theta, phi], tick_labels=["r", "theta", "phi"])
    plt.title("Boxplot der Koordinaten")
    plt.ylabel("Wert")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()

analyze_data()