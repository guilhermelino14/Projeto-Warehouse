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
        if num_forklifts == 1:
            cut1_ind1 = cut1_ind2 = 0
            cut2_ind1 = cut2_ind2 = num_genes-1
            count_child1__0 = count_child2__0 = 0
        else:
            forkliftToRecombine = GeneticAlgorithm.rand.randint(1, num_forklifts)
            cut1_ind1, cut2_ind1, count_child1__0 = self.computeCuts(ind1, forkliftToRecombine)
            cut1_ind2, cut2_ind2, count_child2__0 = self.computeCuts(ind2, forkliftToRecombine)



        child1 = [-1] * num_genes
        for i in range(cut1_ind1, cut2_ind1+1):
            child1[i] = ind1.genome[i]

        j = cut2_ind2+1
        if j == num_genes:
            j = 0
        for i in range(cut2_ind1+1, num_genes):
            if child1[i] == -1:
                while child1.__contains__(ind2.genome[j]):
                    if ind2.genome[j] == 0 and count_child1__0 < num_forklifts-1:
                        count_child1__0 += 1
                        break
                    j += 1
                    if j == num_genes:
                        j=0
                child1[i] = ind2.genome[j]

        for i in range(cut1_ind1):
            if child1[i] == -1:
                while child1.__contains__(ind2.genome[j]):
                    if ind2.genome[j] == 0 and count_child1__0 < num_forklifts-1:
                        count_child1__0 += 1
                        break
                    j += 1
                    if j == num_genes:
                        j=0
                child1[i] = ind2.genome[j]

        child2 = [-1] * num_genes
        for i in range(cut1_ind2, cut2_ind2+1):
            child2[i] = ind2.genome[i]
        j = cut2_ind1+1
        if j == num_genes:
            j = 0
        for i in range(cut2_ind2+1, num_genes):
            if child2[i] == -1:
                while child2.__contains__(ind1.genome[j]):
                    if ind1.genome[j] == 0 and count_child2__0 < num_forklifts-1:
                        count_child2__0 += 1
                        break
                    j += 1
                    if j == num_genes:
                        j=0
                child2[i] = ind1.genome[j]
        for i in range(cut1_ind2):
            if child2[i] == -1:
                while child2.__contains__(ind1.genome[j]):
                    if ind1.genome[j] == 0 and count_child2__0 < num_forklifts-1:
                        count_child2__0 += 1
                        break
                    j += 1
                    if j == num_genes:
                        j=0
                child2[i] = ind1.genome[j]




        ind1.genome = child2
        ind2.genome = child1

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"

    def computeCuts(self, ind : Individual, forkliftToRecombine):
        if forkliftToRecombine == 1:
            for i in range(len(ind.genome)):
                if ind.genome[i] == 0:
                    return 0, i, 1
            return 0, ind.num_genes - 1, 0

        count = 1
        for i in range(len(ind.genome)):
            if ind.genome[i] == 0:
                count += 1
                if count == forkliftToRecombine:
                    cut1 = i

        for i in range(cut1+1, len(ind.genome)):
            if ind.genome[i] == 0:
                return cut1, i, 2
        return cut1, ind.num_genes - 1, 1