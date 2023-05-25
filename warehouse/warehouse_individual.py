import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.pair import Pair
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.paths = self.problem.agent_search.pairs
        self.products = self.problem.products # produtos a coletar
        self.all_path = [[] for _ in range(len(self.problem.forklifts))]
        # TODO

    def compute_fitness(self) -> float:
        # TODO

        current_cell = self.problem.agent_search.forklifts[0]
        self.all_path[0].append(current_cell)
        last_cell = self.problem.agent_search.exit
        self.fitness = 0

        for gene in self.genome:
            product_cell = self.products[gene-1]
            current_cell = self.aux_fitness(current_cell, product_cell)
            self.all_path[0].append(current_cell)

        current_cell = self.aux_fitness(current_cell, last_cell)
        self.all_path[0].append(current_cell)


        return self.fitness

    def aux_fitness(self, current_cell, destination_cell) -> Cell:
        for path in self.paths:
            if path == Pair(current_cell, destination_cell):
                self.fitness += path.value
                return destination_cell

    def obtain_all_path(self):
        # TODO
        # calcular os caminhos completos percorridos pels forklifts, devolve uma lista de listas de celulas e o numero
        # maximo de passos necessarios para percorrer todos os caminhos
        return self.all_path, self.num_genes+2

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genes: ' + str(self.genome) + '\n'
        string += 'Paths: \n'
        for cell in self.all_path[0]:
            string += str(cell.line) + ":" + str(cell.column) + "\n"
        string += "\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance