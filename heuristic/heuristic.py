from utils.__instance__ import MAX_CAPACITY, NUM_ITEMS
from utils.solution import Solution

# import cell
from heuristic.cell import Cell


def add_optimal(DP, k):
    optimal_cell = DP[k-1].get_optimal()
    DP.append(optimal_cell)


def get_solution(DP, num_items):
    solution = Solution(num_bins=DP[-1].num_bins)

    for i in range(num_items):
        solution.add_item_idx(DP[i].item_size, DP[i].insert_idx)

    return solution


def init_heuristic(item_sizes):
    item_sizes.sort(reverse=True)
    num_items = NUM_ITEMS
    DP = [Cell.create_cell(item_sizes, 0)]

    return DP, num_items


def heuristic(item_sizes):

    DP, num_items = init_heuristic(item_sizes)

    for k in range(1, num_items):
        add_optimal(DP, k)

    return DP
