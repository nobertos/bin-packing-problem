from simulated_annealing import simulated_annealing, tweak
def simulated_annealing_test():
    items =[35, 35, 34, 34, 34, 33, 33, 33, 32, 31, 31, 30, 30, 29, 28, 28, 28, 27, 26, 26, 26, 26, 25, 25, 22, 22, 21, 20, 18, 18, 16, 16, 16, 16, 16, 13, 13, 13, 12, 11, 11, 10, 10, 9, 9, 7, 7, 7, 7, 5]
    print(f"Items length {len(items)}")
    input()
    solution = simulated_annealing(items,time=100000, temperature=10000, schedule=10)

    print(solution)
    print(f"length of solution: {len(solution)}")



def tweak_test():
    items = [[12,1],[9,10]]

    print(items)

    input()

    solution = tweak(items)

    print()
    print(solution)


tweak_test()


