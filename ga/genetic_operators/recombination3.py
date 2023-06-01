from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # [1, 3, |0, 2, 5, 4, 0, 8, 7, 6]
        # [2, 1, 3, |0, 6, 0, 7, 4, 5, 6]
        num_genes = ind1.num_genes
        num_forklifts = len(ind1.problem.forklifts)
        forkliftToRecombine = GeneticAlgorithm.rand.randint(1, num_forklifts)

        cut1_ind1 = self.cut1(ind1, forkliftToRecombine)
        #cut2_ind1 = self.cut2(ind1, cut1_ind1)

        cut1_ind2 = self.cut1(ind2, forkliftToRecombine)
        #cut2_ind2 = self.cut2(ind2, cut1_ind2)

        child1 = [-1] * num_genes
        for i in range(cut1_ind1+1):
            child1[i] = ind1.genome[i]
        j = cut1_ind2
        for i in range (cut1_ind1+1, num_genes):
            j += 1
            if j == num_genes:
                j = 0
            child1[i] = ind2.genome[j]


        child2 = [-1] * num_genes
        for i in range(cut1_ind2+1):
            child2[i] = ind2.genome[i]
        j = cut1_ind1
        for i in range(cut1_ind2+1, num_genes):
            j += 1
            if j == num_genes:
                j = 0
            child2[i] = ind1.genome[j]


        ind1.genome = child2
        ind2.genome = child1

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"

    def cut1(self, ind : Individual, forkliftToRecombine):
        if forkliftToRecombine == 1:
            return -1
        count = 1
        for i in range(len(ind.genome)):
            if ind.genome[i] == 0:
                count += 1
                if count == forkliftToRecombine:
                    return i

    def cut2(self, ind : Individual, cut1):
        return -1
        for i in range(cut1, len(ind.genome)):
            if ind.genome[i] == 0:
                return i
        return ind.num_genes - 1