import numpy as np

from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int, products: []):
        super().__init__(problem, num_genes)
        self.paths = self.problem.agent_search.pairs
        self.products = products # produtos a coletar
        # TODO

    def compute_fitness(self) -> float:
        # TODO
        self.fitness = len(self.products) * 10
        last_cell = None
        produtos_recolhidos = np.full(len(self.products), False, dtype=bool)
        cell_exit = self.problem.agent_search.exit
        cell_forklift = self.problem.agent_search.forklifts[0]
        sort_indices = np.argsort(self.genome)

        for i in sort_indices:
            if self.genome[i] > 0: # Os genes ativos sao maiores que 0 e vai por
                #1
                self.fitness += self.paths[i].value # vai ao numero do gene que representa o nº do caminho

                #2 Pontos pelo produto que ainda nao foi apanhado
                for j in range(len(self.products)):
                    if self.products[j] == self.paths[i].cell2: #se a cell pa onde vai é um produto
                        if produtos_recolhidos[j] == False: # se ainda nao apanhou o produto
                            produtos_recolhidos[j] = True
                            self.fitness -= 10

                #3 "teleporte"
                if last_cell is not None:
                    if last_cell != self.paths[i].cell1:
                        self.fitness += 25
                    # vai aumentar o fitness 10 pq o carrinho dá "teleportes"
                    # quando o ultima cell nao é a mesma do proximo caminho

                #4 primeira celula ser a inicial do forklift
                else:
                    if self.paths[i].cell1 != cell_forklift:
                        self.fitness += 50
                last_cell = self.paths[i].cell2
                i = 0

        #5 se o ultimo caminho que ele vai é a saida o fitness
        if last_cell != cell_exit:
            self.fitness += 50
        print(self.fitness)
        return self.fitness

    def obtain_all_path(self):
        # TODO
        self.paths = self.problem.agent_search.pairs
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genes: ' + str(self.genome) + '\n'
        string += 'Paths: \n'
        sort_indices = np.argsort(self.genome)
        for i in sort_indices:
            if self.genome[i] > 0:
                string += str(self.paths[i].cell1.line) + ":" + str(self.paths[i].cell1.column) + "->" + str (self.paths[i].cell2.line) + ":" + str(self.paths[i].cell2.column) + " - cost (" + str(self.paths[i].value) + ")\n"
        string += "\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes, self.products)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance