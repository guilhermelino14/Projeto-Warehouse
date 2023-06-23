from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        #order crossover
        num_genes = ind1.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        #print("BEFORE " + str(ind1.genome) + " - " + str(ind2.genome))

        mapping1 = ind1.genome[cut1:cut2 + 1]
        mapping2 = ind2.genome[cut1:cut2 + 1]

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind2.genome)

        child1[cut1:cut2 + 1] = mapping2
        child2[cut1:cut2 + 1] = mapping1

        index1 = (cut2 + 1) % len(ind1.genome)
        while -1 in child1:
            if ind1.genome[index1] not in child1:
                child1[child1.index(-1)] = ind1.genome[index1]
            index1 = (index1 + 1) % len(ind1.genome)

        index2 = (cut2 + 1) % len(ind2.genome)
        while -1 in child2:
            if ind2.genome[index2] not in child2:
                child2[child2.index(-1)] = ind2.genome[index2]
            index2 = (index2 + 1) % len(ind2.genome)

        #print("AFTER " + str(child1) + " - " + str(child2))

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
