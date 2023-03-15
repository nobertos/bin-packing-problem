from utils.solution import Solution
from utils.__instance__ import MAX_CAPACITY
from branch_bound.evaluation import evaluate3 as evaluate
# to use this version of the code, you need to prune when child.lower_bound >= best_num_bins


class Node:
    def __init__(self, item_size=0, remaining_items=[], parent=None):
        self.item_size = item_size
        self.remaining_items = remaining_items
        self.parent = parent
        self.bin_added = item_size > parent.remaining_capacity if parent is not None else False
        self.calc_remaining_capacity()

        self.num_bins = parent.num_bins + self.bin_added if parent is not None else 0
        self.lower_bound = evaluate(self.num_bins, self.remaining_items)

    def calc_remaining_capacity(self):
        if self.bin_added:
            self.remaining_capacity = MAX_CAPACITY - self.item_size
        elif self.parent is not None:
            self.remaining_capacity = self.parent.remaining_capacity - self.item_size
        else:
            self.remaining_capacity = 0

    def is_leaf(self):
        return len(self.remaining_items) == 0

    def get_solution(self, items1):

        solution = Solution()
        solution.add_items(items1)
        node = self

        while node.parent is not None:
            solution.add_item(node.item_size)
            node = node.parent

        return solution
