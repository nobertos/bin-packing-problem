MAX_CAPACITY = 10
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
