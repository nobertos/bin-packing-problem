from typing import List
with open("utils/__instance__.txt", "r") as f:
    lines = f.readlines()
    NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[1].strip())
    INPUT_ITEMS: List[int] = [int(line.strip()) for line in lines[2:]]

MAX_CAPACITY = 70
INPUT_ITEMS = [44, 6, 24, 6, 24, 8, 22, 8, 17, 21]
NUM_ITEMS = len(INPUT_ITEMS)
print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
