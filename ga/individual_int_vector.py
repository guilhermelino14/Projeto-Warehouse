
from abc import abstractmethod

import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # [3,1,2]
        # [1-3, A1, B2, B4]
        # [A1, B3, B4, B2]
        # [0, A1, B2, 0] [B3, A1, B2, A1]
        # [0, B3, B4, 0] [A1, B3, B4, A3]
        self.num_forklifts = len(self.problem.forklifts)

        lista = np.arange(1, num_genes+1)
        lista = np.random.permutation(lista)

        self.genome = [str(valor) for valor in lista]
        produtos_atribuidos = 0
        prob = 0.5
        while (produtos_atribuidos != num_genes):
            for forklift in range(1, len(self.problem.forklifts)+1):
                for i in range(num_genes):
                    if GeneticAlgorithm.rand.random() > prob and self.genome[i].isdigit():
                        self.genome[i] = (str(forklift) + "-" + self.genome[i])
                        produtos_atribuidos += 1
            prob -= 0.1
        # TODO

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
