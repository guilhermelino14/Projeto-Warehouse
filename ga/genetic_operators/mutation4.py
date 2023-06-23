import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

WITHOUT_LAST_SEPARTOR = 4

WITH_BOTH_SEPARATORS = 3

WITHOUT_FIRST_SEPARATOR = 2

WITHOUT_SEPARATORS = 1


class Mutation4(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:

        print("BEFORE " + str(ind.genome))
        num_forklifts = len(ind.problem.forklifts)
        
        forkliftToRecombine = GeneticAlgorithm.rand.randint(1, num_forklifts)
        cut1, cut2, separator_type = self.computeCuts(ind, forkliftToRecombine)
        if separator_type == WITHOUT_SEPARATORS:
            GeneticAlgorithm.rand.shuffle(ind.genome)
            return
        if separator_type == WITHOUT_FIRST_SEPARATOR:
            parte1 = np.array([], dtype=int)
            parte2 = ind.genome[cut1:cut2]
            parte3 = ind.genome[cut2:]
        if separator_type == WITHOUT_LAST_SEPARTOR:
            parte1 = ind.genome[:cut1+1]
            parte2 = ind.genome[cut1 + 1:cut2+1]
            parte3 = np.array([], dtype=int)
        if separator_type == WITH_BOTH_SEPARATORS:
            parte1 = ind.genome[:cut1 + 1]
            parte2 = ind.genome[cut1 + 1:cut2]
            parte3 = ind.genome[cut2:]

        GeneticAlgorithm.rand.shuffle(parte2)

        array_permutado = np.concatenate((parte1, parte2, parte3)).astype(int) # problema qd apenas uma parte esta preenchida o numpy mete os valores como numpy.float64

        ind.genome = array_permutado

        print("AFTER " + str(ind.genome))




    def __str__(self):
        return "Mutation 4 (" + f'{self.probability}' + ")"

    def computeCuts(self, ind : Individual, forkliftToRecombine):
        last_product = len(ind.problem.products) # os last_productes sao depois do ultimo produto
        if forkliftToRecombine == 1:
            for i in range(len(ind.genome)):
                if ind.genome[i] > last_product:
                    return 0, i, WITHOUT_FIRST_SEPARATOR
            return 0, ind.num_genes - 1, WITHOUT_SEPARATORS

        count = 1 #forklift count
        for i in range(len(ind.genome)):
            if ind.genome[i] > last_product:
                count += 1
                if count == forkliftToRecombine:
                    cut1 = i

        for i in range(cut1+1, len(ind.genome)):
            if ind.genome[i] > last_product:
                return cut1, i, WITH_BOTH_SEPARATORS
        return cut1, ind.num_genes - 1, WITHOUT_LAST_SEPARTOR