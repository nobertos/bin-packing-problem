from utils.__instance__ import MAX_CAPACITY, NUM_ITEMS
from utils.solution import Solution

# import cell
from dynamic_programming.cell import Cell

"""
    Xk : l'ensemble des objets qu'on peut insérer dans le dernier bin.
    Bk : l'ensemble des capacités restantes dans le dernier bin à la fin de l'étape k, càd après l'insertion de l'objet xk.
    Ck (cost) : B(k-1) x Xk --> {0, 1}
         (b(k-1), xk) --> 1 - b(k-1) div xk
        b(k-1) : la capacité restante dans le dernier bin à la fin de l'étape k-1
        xk : la taille de l'objet k
    Tk (transform) : B(k-1) x Xk --> Bk
        (b(k-1), xk) --> bk = b(k-1) - xk si xk <= b(k-1) sinon B - xk
"""
"""
    the psuedo code is as follows:
    B0 = {0, 0, ..., 0} len(B0) = n
    X0 = {x1, x2, ..., xn} len(X0) = n
    C0 = {0, 0, ..., 0} len(C0) = n

    for k = 1 to n:
        for i = 1 to n:
            if i == 1:
                


"""


def add_optimal(DP, k, i):
    optimal_cell = DP[k-1][i].get_optimal()
    DP[k].append(optimal_cell)


def get_min_cost(DP):
    min_cost = DP[-1][0].cost
    min_idx = 0
    for (i, cell) in enumerate(DP[-1]):
        if cell.cost < min_cost:
            min_cost = cell.cost
            min_idx = i
    return min_idx, min_cost


def get_solution(DP, num_items):
    min_idx, _ = get_min_cost(DP)
    solution = Solution()

    for i in range(num_items):
        solution.add_item(DP[i][min_idx].item_size)

    return solution


def init_dyn_programming(item_sizes):
    item_sizes.sort(reverse=True)
    num_items = NUM_ITEMS
    # init step 1
    DP = [[Cell.create_cell(item_sizes, i, cost=1) for i in range(num_items)]]

    return DP, num_items


def dynamic_programming(item_sizes):
    """
    item_sizes: list of item sizes
    cost_matrix: cost_matrix[k][i] = cost of inserting item_sizes[i] in the last bin
    transform_matrix: transform_matrix[k][i] = remaining capacity of the last bin after inserting item_sizes[i]
    """
    DP, num_items = init_dyn_programming(item_sizes)

    for k in range(1, num_items):
        DP.append([])
        for i in range(num_items):
            # print(f"step {k}, item {i}, {DP[k][i]}")
            add_optimal(DP, k, i)

    return DP
