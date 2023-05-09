import numpy as np
import random as rd
from local_search.heuristics import  best_fit, first_fit, next_fit, space
def simulated_annealing(items,  temperature, time, schedule ):
    temperature = temperature
    solution: list[list[int]]= best_fit(items)
    best = solution
    time = time
    num_change = 0
    while True:
        temp = tweak(solution)
        rand = np.random.rand()
        quality_solution = quality(solution)
        quality_temp = quality(temp)
        delta = quality_temp - quality_solution
        if delta > 0 or (rand < np.exp(delta/temperature)):
            num_change += 1
            solution = temp
        temperature = decrease(temperature, schedule)
        time -= 1 
        if (quality_solution > quality(best)):
            best = solution

        if (time==0 or temperature <= 1):
            break


    print(f"number of changes {num_change}")

    return best


def decrease(temperature, schedule):
    return temperature / (1 + schedule* temperature)

def quality(solution):
    objective_function = 0
    for bin in solution:
        bin_load = sum(bin)
        objective_function += bin_load ** 2

    return objective_function

def tweak(solution):
    neighbor = []
    for bin in solution:
        neighbor.append(bin[:])
    bin_indices = list(range(len(neighbor)))
    bin_idx = rd.choice(bin_indices)
    bin_indices.remove(bin_idx)
    bin = neighbor[bin_idx]

    removed_item_idx = rd.randrange(len(bin))
    removed_item=  bin[removed_item_idx]
    del bin[removed_item_idx]
    space_bin = space(bin)

    while True:
        if len(bin_indices) == 0 :
            new_bin = []
            new_bin.append(removed_item)
            neighbor.append(new_bin)
            break

        temp_bin_idx = rd.choice(bin_indices)
        bin_indices.remove(temp_bin_idx)
        temp_bin = neighbor[temp_bin_idx]

        if space(temp_bin) - removed_item >= 0:
            temp_bin.append(removed_item)
            break
        exchanged = False
        for (item_idx, item) in enumerate(temp_bin):
            if (space(temp_bin) + item - removed_item)>= 0 and (space_bin - item >= 0):
                bin.insert( removed_item_idx, item)
                del temp_bin[item_idx]

                temp_bin.insert(item_idx, removed_item)
                exchanged = True
                break
        if exchanged:
            break
    if len(bin) == 0 :
        del neighbor[bin_idx]
    return neighbor



