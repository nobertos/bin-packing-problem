
from utils.instance import MAX_CAPACITY
import math


class Cell:
    def __init__(self, item_size=0,  remaining_capacities=[], remaining_items=[]):
        self.item_size = item_size
        self.remaining_items = remaining_items
        self.remaining_capacities = remaining_capacities
        self.insert_idx = self.calc_next(item_size)
        self.num_bins = len(self.remaining_capacities)

    def __repr__(self) -> str:
        return f"Cell: inserted item {self.item_size}, num_bins {self.num_bins}, remaining_items {self.remaining_items} "

    def calc_next(self, item_size):
        min_idx = 0
        best_capacity = math.inf
        for (i, capacity) in enumerate(self.remaining_capacities):
            if item_size <= capacity and capacity <= best_capacity:
                best_capacity = capacity
                min_idx = i
        if best_capacity != math.inf:
            self.remaining_capacities[min_idx] -= item_size
            return min_idx
        self.remaining_capacities.append(MAX_CAPACITY - item_size)
        return len(self.remaining_capacities) - 1

    def remove_item(self, index):
        self.remaining_items.pop(index)

    def get_optimal(self):
        return self.create_cell(self.remaining_items, 0, self.remaining_capacities)

    @staticmethod
    def create_cell(items, removed_position, remaining_capacities=[]):
        remaining_items = items[:]
        remaining_items.pop(removed_position)
        return Cell(item_size=items[removed_position], remaining_items=remaining_items, remaining_capacities=remaining_capacities)
