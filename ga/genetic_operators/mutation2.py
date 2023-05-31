from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # trocar o agente de um gene do gnome por outro agente
        num_agent = ind.num_forklifts
        num_genes = len(ind.genome)
        i = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        agent = ind.genome[i].split("-")[0]
        new_agent = GeneticAlgorithm.rand.randint(1, num_agent)
        while agent == new_agent:
            new_agent = GeneticAlgorithm.rand.randint(1, num_agent)

        ind.genome[i] = str(new_agent) + "-" + ind.genome[i].split("-")[1]

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
