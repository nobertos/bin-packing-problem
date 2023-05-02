import numpy as np
import random as rd
from first_fit import first_fit, space
def simulated_annealing(items, ideal_quality=None, temperature=1, time=10000, schedule = 0.1):
    temperature = temperature
    solution: list[list[int]]= first_fit(items)
    print(f"first_fit solution :{solution}")
    best = solution
    time = time
    ideal_quality = ideal_quality if ideal_quality != None else 1
    num_change = 0
    while True:
        temp = tweak(solution)
        rand = np.random.rand()
        quality_solution = quality(solution)
        quality_temp = quality(temp)
        if (quality_temp > quality_solution or (rand < np.exp(( quality_temp - quality_solution)/temperature))):
            num_change += 1
            solution = temp
        temperature -= schedule * temperature
        time -= 1 
        if (quality_solution < quality(best)):

            num_change +=1
            best = solution

        if (best == ideal_quality or time==0 or temperature <= 0):
            break

    print(f"number of changes {num_change}")
    return best



def quality(solution):
    sum = 0
    for bin in solution:
        sum += space(bin)
    return 1/sum

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

        exchanged = False
        for (item_idx, item) in enumerate(temp_bin):
            if (space(temp_bin) + item - removed_item)>= 0 or (space_bin - item >= 0):
                bin.insert( removed_item_idx, item)
                del temp_bin[item_idx]
                temp_bin.insert(item_idx, removed_item)
                exchanged = True
                break
        if exchanged:
            break
    return neighbor



