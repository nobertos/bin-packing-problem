from typing import List
with open("utils/__instance__.txt", "r") as f:
    lines = f.readlines()
    NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[1].strip())
    INPUT_ITEMS: List[int] = [int(line.strip()) for line in lines[2:]]

MAX_CAPACITY = 100
INPUT_ITEMS = [99, 94, 79, 64, 50, 44, 43, 37, 32, 19, 18, 7, 3]
NUM_ITEMS = len(INPUT_ITEMS)
print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
