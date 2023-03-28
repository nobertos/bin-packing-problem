import time
from branch_bound.branch_bound import branch_and_bound
from heuristic.heuristic import heuristic, get_solution
from utils.solution import Solution
from utils.__instance__ import INPUT_ITEMS, NUM_ITEMS


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def first_solution(item_sizes):
    solution = Solution()
    for item_size in item_sizes:
        solution.add_item(item_size)
    return solution


def main():
    # calculate the time
    time_list = [time.time()]
    first_sol = first_solution(INPUT_ITEMS)
    time_list.append(time.time())
    print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}---------------------------------------{bcolors.ENDC}\n")
    print(
        f"\n{bcolors.WARNING}{bcolors.BOLD}First Solution:{bcolors.ENDC} {first_sol.num_bins}, time: {time_list[1] - time_list[0]}\n")
    print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}---------------------------------------{bcolors.ENDC}\n")

    heuristic_res = get_solution(heuristic(INPUT_ITEMS), NUM_ITEMS)
    time_list.append(time.time())
    print(
        f"\n{bcolors.WARNING}{bcolors.BOLD}Heuristic:{bcolors.ENDC} {heuristic_res}, time: {time_list[2] - time_list[1]}\n")
    print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}---------------------------------------{bcolors.ENDC}\n")
    branch_bound = branch_and_bound(INPUT_ITEMS)
    time_list.append(time.time())
    print(
        f"\n{bcolors.WARNING}{bcolors.BOLD}Branch and bound:{bcolors.ENDC} {branch_bound}, time: {time_list[3] - time_list[2]}")


if __name__ == "__main__":
    main()
