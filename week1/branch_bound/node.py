from utils.solution import Solution
from utils.__instance__ import MAX_CAPACITY
import math
# to use this version of the code, you need to prune when child.lower_bound >= best_num_bins


class Node:
    def __init__(self, item_size=0, remaining_items=[], parent=None):
        self.item_size = item_size
        self.remaining_items = remaining_items
        self.parent = parent
        self.remaining_capacity = self.calc_remaining_capacity()
        self.num_bins = parent.num_bins + \
            (item_size > parent.remaining_capacity) if parent is not None else 0

    def calc_remaining_capacity(self):
        if self.parent is not None:
            parent_capacity = self.parent.remaining_capacity
            if self.item_size > parent_capacity:
                return MAX_CAPACITY - self.item_size
            return parent_capacity - self.item_size
        return 0

    def separate(self):
        bound1 = MAX_CAPACITY - self.remaining_items[-1]
        bound2 = MAX_CAPACITY//2
        len_items1 = 0
        len_items2 = 0
        sum_items2 = 0
        sum_items3 = 0
        remaining_capacity = self.remaining_capacity
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
        return len_items1 + len_items2 + max(0, math.ceil((sum_items3 - (len_items2*MAX_CAPACITY - sum_items2))/MAX_CAPACITY))

    def lower_bound(self):
        return self.num_bins + self.evaluation_fn()

    def is_leaf(self):
        return len(self.remaining_items) == 0

    def get_solution(self):
        solution = Solution()
        node = self
        while node.parent is not None:
            solution.add_item(node.item_size)
            node = node.parent
        return solution
