from math import pow
import numpy as np
import pandas as pd


class AntColony(): 
    def __init__(
                self,
                items: list[int],
                max_capacity: int,
                num_ants: int,
                num_iteration: int,
                decay: float,
                 beta: int,
                 ) -> None:
        self.items = items
        self.num_items = len(items)
        self.max_capacity = max_capacity
        self.num_ants = num_ants
        self.num_iteration = num_iteration
        self.decay = decay
        self.beta = beta
        self.pheromones = self.__init_pheromones(items)

    def __init_pheromones(self, items: list[int]) -> np.ndarray:
        return np.ones(
            [len(items), len(items)],
            dtype=np.float128
        ) 
    def fitness(self, solution) -> float:
        fit = 0
        for bin in solution:
            bin_weight = self.max_capacity - self.space(bin)
            fit += bin_weight ** 2
        fit = fit/(self.max_capacity*self.num_items)
        return fit

    def low_pheromone(self, prob_best, evaporation_rate):
        nomenator = (1/(1-evaporation_rate)) * (1 - pow(prob_best, 1/self.num_items))
        denomenator = (self.num_items/2 - 1) * pow(prob_best, 1/self.num_items)
        return nomenator/denomenator

    def decay_pheromones(self):
        self.pheromones = self.pheromones * self.decay

    def get_pheromone(self, item_idx: int, bin: list[int])-> float:
        len_bin = len(bin)
        if len_bin == 0:
            return 1
        pheromone_sum = 0
        for tmp_item_idx in range(len_bin):
            pheromone_sum += self.pheromones[tmp_item_idx][item_idx] 
        return float(pheromone_sum/len_bin)

    def prob_take(self, free_space: int, item_idx, idx, bin, items: list[tuple[int,int]] ) -> float:
        """
            space_left:  space that is left in the bin
        """
        if  items[idx][1] > free_space:
            return 0.0
        numerator = self.get_pheromone(item_idx, bin) * (items[idx][1]**self.beta)
        denomenator = 0
        for  tmp_item in items:
            if tmp_item[1] <= free_space:
                denomenator = denomenator +  self.get_pheromone(tmp_item[0], bin) * (tmp_item[1] ** self.beta)
        return numerator / denomenator

    def can_place_item_bin( self,free_space, item_idx, idx, bin, items) -> bool:
        random = np.random.uniform()
        probability = self.prob_take(free_space, item_idx,idx, bin, items)
        return  (random < probability)

    
    def space(self,bin):
        bin_weight = 0
        for (_, item) in bin:
            bin_weight+=item
        return self.max_capacity -bin_weight 

    def push_items(self, items) -> list[tuple[int, int]]:
        bin: list[tuple[int,int]] = []
        free_space = self.max_capacity
        idx = 0
        while True:
            if len(items) == 0 or free_space < items[-1][1]:
                break
            if idx == len(items):
                idx = 0
            item_idx, item = items[idx]
            if self.can_place_item_bin(free_space,item_idx, idx,bin, items):
                bin.append((item_idx, item))
                free_space -= item
                del items[idx]
                continue
            idx +=1
        if len(bin) == 0:
            print("lenbin ", idx, len(items))
        return bin

    def create_solution(self) -> list[list[tuple[int, int]]]:
        items = []
        for (item_idx, item) in enumerate(self.items):
            items.append((item_idx, item))
        solution = []
        while True:
            if len(items) == 0:
                break
            bin = self.push_items(items)
            solution.append(bin)
        return solution


    def run_ants(self):
        solutions  = [None]*self.num_ants
        for ant_idx in range(self.num_ants):
            solution = self.create_solution()
            solutions[ant_idx] = (solution, self.fitness(solution))
        return solutions


    def update_pheromones(self, best_solution: tuple):
        best = best_solution[0]
        best_fitness = best_solution[1]

    
        for bin in best:
            for (item_bin_idx, (item_idx,_)) in enumerate(bin):
                for (next_item_idx,_) in bin[item_bin_idx+1:]:
                    self.pheromones[item_idx, next_item_idx] += best_fitness
                    self.pheromones[next_item_idx, item_idx] += best_fitness

    def solve(self) -> tuple[list, float]:
        iteration_best = ([],0) 
        global_best = None

        for it in range(self.num_iteration):
            solutions = self.run_ants()
            self.decay_pheromones()
            iteration_best = max(solutions, key=lambda x: x[1])
            if it % 5 ==0 and it >0:
                self.update_pheromones(global_best)
            else:
                self.update_pheromones(iteration_best)
            print(f"Iteration #{it}; Best iteration solution: {len(iteration_best[0])}")
            if global_best is None or iteration_best[1] > global_best[1]:
                global_best = iteration_best
        df = pd.DataFrame(self.pheromones)
        print(df)
        return global_best
