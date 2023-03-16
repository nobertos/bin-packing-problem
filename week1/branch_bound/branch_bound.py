
from collections import deque
from branch_bound.node import Node
from utils.__instance__ import MAX_CAPACITY

# import Node class from node.py


def create_node(item_size, posistion, remaining_items, parent):
    remaining_items = remaining_items.copy()
    remaining_items.pop(posistion)
    return Node(item_size, remaining_items, parent)


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

    root = Node(remaining_items=item_sizes)
    active_nodes = deque()
    active_nodes.append(root)
    best_num_bins = len(item_sizes) + 1
    return active_nodes, best_num_bins


def branch_and_bound(item_sizes):

    active_nodes, best_num_bins = init_branch_and_bound(
        item_sizes)
    optimal_node = None
    num_iterations = 0
    num_pruned = 0
    print(f"Initial best solution")

    while active_nodes:
        num_iterations += 1
        node = active_nodes.pop()
        if node.lower_bound() >= best_num_bins:
            num_pruned += 1
            continue
        for (i, current_item) in enumerate(node.remaining_items):
            child = create_node(
                current_item, i, node.remaining_items, node)
            if child.is_leaf():
                if child.num_bins < best_num_bins:
                    print(f"Found better solution")
                    best_num_bins = child.num_bins
                    optimal_node = child
                continue
            active_nodes.append(child)

    print(f"Number of pruned nodes: {num_pruned}")
    print(f"Number of iterations: {num_iterations}")

    return optimal_node.get_solution() if optimal_node is not None else None
