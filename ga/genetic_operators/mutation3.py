from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        #print("BEFORE " + str(ind.genome))
        # selecionar aleatoriamente dois índices diferentes no genoma do indivíduo
        index1 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        index2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        while index2 == index1:
            index2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        # Troque os valores nos índices selecionados
        ind.genome[index1], ind.genome[index2] = ind.genome[index2], ind.genome[index1]
        #print("AFTER " + str(ind.genome))

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
