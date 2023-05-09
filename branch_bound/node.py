from utils.solution import Solution
from utils.instance import MAX_CAPACITY
import math
from typing import List
from enum import Enum


class order(Enum):
    FIT_ITEM = 0
    ADD_BIN = 1


class Node:
    def __init__(self, item_size=0, remaining_items=[], parent=None, order=None, inserted_idx=None):
        self.item_size = item_size
        self.remaining_items = remaining_items[:]
        self.parent = parent
        self.order = order
        self.remaining_capacities = parent.remaining_capacities[:] if parent is not None else [
        ]
        self.num_bins = parent.num_bins if parent is not None else 0
        self.inserted_idx = inserted_idx
        self.calc_remaining_capacities()

    def calc_remaining_capacities(self):
        if self.parent is not None:
            if self.order == order.ADD_BIN:
                self.remaining_capacities.append(MAX_CAPACITY-self.item_size)
                self.inserted_idx = self.num_bins
                self.num_bins += 1
                return
            self.remaining_capacities[self.inserted_idx] -= self.item_size
            return

    def does_fit(self, item):
        for (i, capacity) in enumerate(self.remaining_capacities):
            if item <= capacity:
                return True
        return False

    def separate(self):
        bound1 = MAX_CAPACITY - self.remaining_items[-1]
        bound2 = MAX_CAPACITY//2
        len_items1 = 0
        len_items2 = 0
        sum_items2 = 0
        sum_items3 = 0
        # reduce the self.remaining_capacities to its sum

        remaining_capacity = sum(self.remaining_capacities)
        for item in self.remaining_items:
            if item <= remaining_capacity:
                remaining_capacity -= item
                continue
            if item > bound1:
                len_items1 += 1
                continue
            if item > bound2:
                len_items2 += 1
                sum_items2 += item
                continue
            sum_items3 += item
        return len_items1, len_items2, sum_items2, sum_items3

    def evaluation_fn(self):
        len_items1, len_items2, sum_items2, sum_items3 = self.separate()
        return len_items1 + len_items2 + max(0, ((sum_items3 - (len_items2*MAX_CAPACITY - sum_items2))/MAX_CAPACITY))

    def evaluation_fn2(self):
        sum = 0
        remaining_capacity = sum(self.remaining_capacities)
        for item in self.remaining_items:
            if item <= remaining_capacity:
                remaining_capacity -= item
                continue
            sum += item

        return sum/MAX_CAPACITY

    def lower_bound(self):
        return self.num_bins + self.evaluation_fn()

    def is_leaf(self):
        return not self.remaining_items

    def get_solution(self):
        solution = Solution(num_bins=self.num_bins)
        node = self
        while node.parent is not None:
            solution.add_item_idx(node.item_size, node.inserted_idx)
            node = node.parent
        return solution
