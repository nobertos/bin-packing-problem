from branch_bound.node import Node, order
from utils.instance import MAX_CAPACITY, NUM_ITEMS
from utils.solution import Solution


def init_branch_and_bound(item_sizes):
    item_sizes.sort(reverse=True)
    root = Node(remaining_items=item_sizes)
    active_nodes = [root]
    root_lb = root.lower_bound()
    print(f"root lower_bound {root_lb}")
    best_num_bins = NUM_ITEMS + 1
    return active_nodes, best_num_bins, root_lb


def branch_and_bound(item_sizes):

    active_nodes, best_num_bins, root_lb = init_branch_and_bound(
        item_sizes)
    optimal_node = None
    num_iterations = 0
    num_pruned = 0
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
        child = Node(current_item, remaining_items, node, order.ADD_BIN)
        active_nodes.append(child)
        if node.does_fit(current_item):
            for (i, capacity) in enumerate(node.remaining_capacities):
                if current_item <= capacity:
                    child = Node(current_item, remaining_items,
                                 node, order.FIT_ITEM, i)
                    active_nodes.append(child)

    print(f"Number of pruned nodes: {num_pruned}")
    print(f"Number of iterations: {num_iterations}")

    return optimal_node.get_solution() if optimal_node is not None else None
