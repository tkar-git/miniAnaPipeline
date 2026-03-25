import random
from typing import List, Tuple

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




