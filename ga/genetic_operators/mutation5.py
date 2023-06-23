from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_operators.mutation4 import Mutation4
from ga.genetic_operators.mutation2 import Mutation2


class Mutation5(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        if len(ind.problem.forklifts) <= 1:
            return
        #print("BEFORE" + str(ind.genome))
        separatorToMutate = GeneticAlgorithm.rand.randint(len(ind.problem.products) + 1, len(ind.genome))
        separatorToMutate_i=0
        while separatorToMutate != ind.genome[separatorToMutate_i]:
            separatorToMutate_i += 1
        product_i = separatorToMutate_i
        while ind.genome[product_i] > len(ind.problem.products):
            product_i = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        ind.genome[separatorToMutate_i], ind.genome[product_i] = ind.genome[product_i], ind.genome[separatorToMutate_i]
        #print("AFTER" + str(ind.genome))
    def __str__(self):
        return "Mutation 5 (" + f'{self.probability}' + ")"