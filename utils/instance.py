from typing import List
with open("utils/instance.txt", "r") as f:
    lines = f.readlines()
    NUM_ITEMS = int(lines[0].strip())
    MAX_CAPACITY = int(lines[1].strip())
    INPUT_ITEMS: List[int] = [int(line.strip()) for line in lines[2:]]

INPUT_ITEMS= [ 35, 35, 34, 34, 34, 33, 33, 33, 32, 31, 31, 30, 30, 29, 28, 28, 28, 27, 26, 26, 26, 26, 25, 25, 22, 22, 21, 20, 18, 18, 16, 16, 16, 16, 16, 13, 13, 13, 12, 11, 11, 10, 10, 9, 9, 7, 7, 7, 7, 5]
MAX_CAPACITY = 50
NUM_ITEMS = 50

print(f"len(INPUT_ITEMS): {NUM_ITEMS}")
