
from utils.__instance__ import MAX_CAPACITY


def calc_cost(remaining_capacity, item_size):
    if item_size <= remaining_capacity:
        return 0
    return 1


def calc_next(remaining_capacity, item_size):
    if item_size <= remaining_capacity:
        return remaining_capacity - item_size
    return MAX_CAPACITY - item_size


class Cell:
    def __init__(self, item_size=0, cost=0, remaining_capacity=0, remaining_items=[]):
        self.item_size = item_size
        self.remaining_items = remaining_items
        self.remaining_capacity = calc_next(remaining_capacity, item_size)
        self.cost = cost

    def __repr__(self) -> str:
        return f"Cell: inserted item {self.item_size}, cost {self.cost}, remaining_items {self.remaining_items}, remaining capacity {self.remaining_capacity}"

    def choose_min(self):
        min_cost = self.cost + \
            calc_cost(self.remaining_capacity, self.remaining_items[0])
        min_idx = 0
        for (i, item_size) in enumerate(self.remaining_items):
            cost = calc_cost(self.remaining_capacity, item_size)
            if cost == 0:
                min_cost = self.cost + cost
                min_idx = i
                break
        return min_idx, min_cost

    def remove_item(self, index):
        self.remaining_items.pop(index)

    def get_optimal(self):
        min_idx, min_cost = self.choose_min()
        remaining_capacity = self.remaining_capacity if self.remaining_items[
            min_idx] <= self.remaining_capacity else MAX_CAPACITY
        return self.create_cell(self.remaining_items, min_idx, min_cost, remaining_capacity)

    @staticmethod
    def create_cell(items, removed_position, cost=0, remaining_capacity=MAX_CAPACITY):
        remaining_items = items.copy()
        remaining_items.pop(removed_position)
        return Cell(item_size=items[removed_position], remaining_items=remaining_items, cost=cost, remaining_capacity=remaining_capacity)
