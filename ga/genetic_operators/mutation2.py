from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # pega num gene e troca-o  para positivo se for negativo e vice versa
        # sendo o negativo desativo e positivo ativo
        num_genes = ind.num_genes
        i_gen = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        ind.genome[i_gen] = -(ind.genome[i_gen])

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
