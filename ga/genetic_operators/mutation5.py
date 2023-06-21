
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_operators.mutation4 import Mutation4
from ga.genetic_operators.mutation2 import Mutation2


class Mutation5(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        Mutation2(ind)
        Mutation4(ind)
    def __str__(self):
        return "Mutation 5 (" + f'{self.probability}' + ")"