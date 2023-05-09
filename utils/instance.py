from typing import List
with open("utils/instance.txt", "r") as f:
    lines = f.readlines()
    NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[1].strip())
    INPUT_ITEMS: List[int] = [int(line.strip()) for line in lines[2:]]
#
INPUT_ITEMS= [ 5,3,2,1]
MAX_CAPACITY = 10
NUM_ITEMS = 4

print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
