import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.pair import Pair
from warehouse.cell import Cell
from warehouse.cell import Adjancente


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.paths = self.problem.agent_search.pairs
        self.products = self.problem.products # produtos a coletar
        self.all_path = [[] for _ in range(len(self.problem.forklifts))]
        # [
        #       []
        #       []
        #       []
        # ]
        self.steps = 0
        # TODO

    def compute_fitness(self) -> float:
        # TODO

        num_forklifts = len(self.problem.forklifts)
        forklift = 0
        current_cell = self.problem.forklifts[forklift] # 1º celula
        last_cell = self.problem.agent_search.exit # celula de saida
        self.fitness = 0

        last_product = len(self.products)

        # [1,3,4,2] o 4 é separador
        for gene in self.genome:
            if gene > last_product:
                self.aux_fitness(current_cell, last_cell)
                forklift +=1
                current_cell = self.problem.forklifts[forklift]
                continue
            product_cell = self.products[gene-1]
            current_cell = self.aux_fitness(current_cell, product_cell,)
        self.aux_fitness(current_cell, last_cell)
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
        self.all_path = [[] for _ in range(len(self.problem.forklifts))]
        self.steps = 0
        steps_aux = 0
        forklift = 0
        current_cell = self.problem.forklifts[forklift]  # 1º celula
        last_cell = self.problem.agent_search.exit  # celula de saida
        self.all_path[forklift].append(current_cell)
        last_product = len(self.products)
        for gene in self.genome:
            if gene > last_product:
                for path in self.paths:
                    if path == Pair(current_cell, last_cell):
                        for i in range(len(path.cells)):
                            self.all_path[forklift].append(path.cells[i])
                        steps_aux += path.steps
                forklift += 1
                current_cell = self.problem.forklifts[forklift]
                self.all_path[forklift].append(current_cell)
                if self.steps < steps_aux:
                    self.steps = steps_aux
                steps_aux = 0
                continue
            product_cell = self.products[gene - 1]
            for path in self.paths:
                if path == Pair(current_cell, product_cell):
                    for i in range(len(path.cells)-1):
                        self.all_path[forklift].append(path.cells[i])
                    self.all_path[forklift].append(Adjancente(path.cells[len(path.cells)-1], path.cell2))
                    steps_aux += path.steps
                    current_cell = product_cell
                    break
        for path in self.paths:
            if path == Pair(current_cell, last_cell):
                for i in range(len(path.cells)):
                    self.all_path[forklift].append(path.cells[i])
                steps_aux += path.steps
        if self.steps < steps_aux:
            self.steps = steps_aux
        return self.all_path, self.steps

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genes: ' + str(self.genome) + '\n'
        string += 'Paths: \n'
        forklift = 0
        current_cell = self.problem.forklifts[forklift]  # 1º celula
        last_cell = self.problem.agent_search.exit  # celula de saida
        last_product = len(self.products)
        for gene in self.genome:
            if gene > last_product:
                forklift += 1
                current_cell = self.problem.forklifts[forklift]
                continue
            for path in self.paths:
                if path == Pair(current_cell, self.products[gene - 1]):
                    current_cell = self.products[gene - 1]
                    string += str(path) + "\n"
                    break
        for path in self.paths:
            if path == Pair(current_cell, last_cell):
                string += str(path) + "\n"
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