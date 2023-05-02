from simulated_annealing import simulated_annealing
def simulated_annealing_test():
    items = [10,8,8,7,5,4,3,3,2,2,1]

    solution = simulated_annealing(items,time=1000000)

    print(solution)


simulated_annealing_test()
    



