import random
from typing import List, Tuple
import csv
#generate random number
def generateRandomnumbers():
    return random.randint(1,10)

def create_coords(*, cols: int, rand_lower: int, rand_upper: int) -> List[Tuple[int, int, int]]:
    coords_list: List[Tuple[int, int, int]] = []
    for i in range(cols):
        # create coords
        x = random.randint(rand_lower, rand_upper)
        y = random.randint(rand_lower, rand_upper)
        z = random.randint(rand_lower, rand_upper)
        print(x, y, z)
        coords_list.append((x, y, z))
    return coords_list
#create 10 numbers
numbers=[generateRandomnumbers() for i in range(10)]

def save_coords(coords:List[Tuple[int, int, int]], filename="data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(coords)  # writerows() writes the entire list at once


if __name__ == "__main__":
    coords = create_coords(cols=100, rand_lower=0, rand_upper=100)
    save_coords(coords)





#write csv file
with open("randomdata.csv",mode="w", newline="") as file:
    writer=csv.writer(file)
    for number in numbers:
        writer.writerow([number])