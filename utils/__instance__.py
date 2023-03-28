from typing import List
with open("utils/__instance__.txt", "r") as f:
    lines = f.readlines()
    NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[1].strip())
    INPUT_ITEMS: List[int] = [int(line.strip()) for line in lines[2:]]


print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
