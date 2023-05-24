
from abc import abstractmethod

import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual


class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = np.arange(1, num_genes+1)
        for i in range(self.num_genes):
            self.genome[i] = -self.genome[i] if GeneticAlgorithm.rand.random() < 0.5 else self.genome[i]
        self.genome = np.random.permutation(self.genome)

        # Este cromossomo vai ser uma sequencia de inteiros que representa o nº do caminho
        # ex: nºgenes(nºde caminhos) [8, 5, -9, 2, -1, -7, 4, -3] gerado aleatoriamente
        # onde os numeros representam a ordem dos caminhos
        # e os nº negativos os genes (os caminhos) que nao estão ativos ->
        #  -> neste caso o primeiro caminho vai ser o quarto (8-4(nºnegativos))
        #  -> a ser executado e o segundo caminho vai ser o terceiro
        #  -> o terceiro nao é executado
        #  -> o quarto vai ser o primeiro ...
        #
        # Nota o operador mutate tera de trocar o numero positivo para negativo
        #                             e vice verca em vez de trocar de 0 para 1
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
