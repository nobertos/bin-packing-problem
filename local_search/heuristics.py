MAX_CAPACITY = 50
def space(bin):
    return MAX_CAPACITY  - sum(bin)


def first_fit(items):
    items.sort(reverse=True)

    solution = [[]]
    for item in items:
        inserted = False
        for bin in solution:
            if space(bin) >= item :
                bin.append(item)
                inserted = True
                break
        if inserted == False:
            new_bin = [item]
            solution.append(new_bin)

    return solution

def next_fit(items):

    solution = [[]]
    for item in items:
        bin = solution[-1]
        if space(bin) >= item :
            bin.append(item)
        else:
            new_bin = [item]
            solution.append(new_bin)

    return solution


def best_fit(items):
    items.sort(reverse=True)

    solution = []
    for item in items:
        min_space = MAX_CAPACITY
        min_idx = len(solution)
        for (bin_idx,bin) in enumerate(solution):
            space_bin = space(bin)
            if space_bin >= item  and space_bin < min_space:
                min_space = space_bin
                min_idx = bin_idx
        if min_space == MAX_CAPACITY:
            new_bin = [item]
            solution.append(new_bin)
        else:
            solution[min_idx].append(item)

    return solution


