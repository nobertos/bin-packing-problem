import numpy as np
from branch_bound.node import Node, order
from utils.__instance__ import MAX_CAPACITY
from utils.solution import Solution
import heartrate
# heartrate.trace(browser=True)
# import Node class from node.py


def create_node(item_size, parent_remaining_items, parent, order):
    remaining_items = parent_remaining_items.copy()
    return Node(item_size, remaining_items, parent, order)


def get_items1(item_sizes):
    min_size = item_sizes[-1]
    items1 = [item for item in item_sizes if item > MAX_CAPACITY - min_size]
    return items1


def remove_items1(item_sizes):
    items1 = get_items1(item_sizes)
    for item in items1:
        item_sizes.remove(item)
    return items1


def init_branch_and_bound(item_sizes):

    item_sizes.sort(reverse=True)
    best_fit = Solution()
    best_fit.best_fit(item_sizes)

    root = Node(remaining_items=item_sizes)
    root_bound = root.lower_bound()
    active_nodes = []
    active_nodes.append(root)
    print(
        f"root lower_bound {root_bound}, remaining items {root.remaining_items}, remaining capacities {root.remaining_capacities}")
    best_num_bins = len(item_sizes)
    return active_nodes, best_num_bins, best_fit


def branch_and_bound(item_sizes):

    active_nodes, best_num_bins, best_fit = init_branch_and_bound(
        item_sizes)
    optimal_node = None
    num_iterations = 0
    num_pruned = 0
    print("\n---------------------------------------\n")
    print(f"Initial best solution {best_num_bins}")

    while active_nodes:
        num_iterations += 1
        node = active_nodes.pop()
        if node.is_leaf():
            if node.num_bins < best_num_bins:
                best_num_bins = node.num_bins
                optimal_node = node
                print(f"Found new best solution {best_num_bins}")
            continue
        if node.lower_bound() >= best_num_bins:
            num_pruned += 1
            continue

        current_item = node.remaining_items[0]
        remaining_items = node.remaining_items[1:]

        child = create_node(
            current_item, remaining_items, node, order=order.ADD_BIN)

        active_nodes.append(child)
        if node.fit(current_item):
            child = create_node(
                current_item, remaining_items, node, order=order.FIT_ITEM)
            active_nodes.append(child)

    print(f"Number of pruned nodes: {num_pruned}")
    print(f"Number of iterations: {num_iterations}")

    return optimal_node.get_solution() if optimal_node is not None else best_fit
