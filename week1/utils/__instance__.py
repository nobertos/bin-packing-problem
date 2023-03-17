from typing import List
with open("utils/__instance__.txt", "r") as f:
    lines = f.readlines()
    # NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[0].strip())
    INPUT_ITEMS = [int(line.strip()) for line in lines[1:]]
    NUM_ITEMS = len(INPUT_ITEMS)

# NUM_ITEMS = 4
# MAX_CAPACITY = 10
# INPUT_ITEMS = [7, 6, 4, 3]

print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
