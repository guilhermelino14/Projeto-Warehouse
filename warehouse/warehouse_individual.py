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
        #       [cell1]
        #       [cell2, cell3, cell4]
        #       [cell5, cell1, cell4]
        # ]
        self.steps = 0
        # TODO

    def compute_fitness(self) -> float:
        # TODO
        self.computePathAndSteps()
        self.fitness = self.steps
        # VER COLISOES
        for i in range(self.steps):
            if self.colisao(self.all_path, i):
                self.fitness += 50
        return self.fitness

    def colisao(self, all_path, indice):
        cells_num_determinado_indice = []
        for forklift_path in all_path:
            if indice > len(forklift_path)-1:
                continue
            cell = forklift_path[indice]
            if cell in cells_num_determinado_indice:
                return True
            cells_num_determinado_indice.append(cell)
        return False

    # def aux_fitness(self, current_cell, destination_cell) -> Cell:
    #     for path in self.paths:
    #         if path == Pair(current_cell, destination_cell):
    #             self.fitness += path.value
    #             return destination_cell

    def obtain_all_path(self):
        # TODO
        self.computePathAndSteps()
        self.steps += 1  # para as celulas iniciais
        return self.all_path, self.steps

    def computePathAndSteps(self):
        # calcular os caminhos completos percorridos pels forklifts, devolve uma lista de listas de celulas e o numero
        # maximo de passos necessarios para percorrer todos os caminhos

        # self.all_path -> array bidimensional com as celulas que corresponde ao caminho de cada forklift
        # self.steps -> passos executados no final
        # steps_forklift -> passos que o forklift currente tem
        # forklift -> indice do forklift currente
        # last_product -> corresponde ao nº do ultimo produto (nota nao é o indice)
        # current_cell -> celula onde "se encontra" o forklift supostamente ao percorrer os genes
        # product_cell -> celula correspondente ao nº do produto representado no gene

        self.all_path = [[] for _ in range(len(self.problem.forklifts))]
        self.steps = steps_forklift = forklift = 0
        last_product = len(self.products)
        current_cell = self.problem.forklifts[forklift]
        # adiciona já a primeira celula ao self_path
        # pq os Pairs.cells nao tem a celula inicial do caminho
        # só é adicionado apos a execucao da açao

        current_cell = self.problem.forklifts[forklift]  # 1º celula
        self.all_path[forklift].append(current_cell)
        for gene in self.genome:
            if gene > last_product:
                # Se é um gene de separacao
                #   vai adicionar o caminho do fork lift ate a saida e aumentar os steps desse forklift
                #   e vai passar para o forklift seguinte e assim preencher o proximo array de celulas
                #   mete logo a celula respondente ao forklift
                #   e verifica se o steps do forklift anterior é superior aos steps
                #       se for maior substitui e reseta os steps_forklift
                steps_forklift += self.addCellsToPath_exit(current_cell, forklift)
                forklift += 1
                current_cell = self.problem.forklifts[forklift]
                self.all_path[forklift].append(current_cell)

                self.checkSteps(steps_forklift)
                steps_forklift = 0
                continue
            # Se nao é uma celula de separacaco chega aki
            # vai buscar product_cell que corresponde ao gene do produto
            # vai adicionar o caminho do fork lift ate a saida e aumentar os steps desse forklift
            # e vai passar a current_cell a ser igual ao  product_cell
            product_cell = self.products[gene - 1]
            steps_forklift += self.addCellsToPath_product(current_cell, product_cell, forklift)
            current_cell = product_cell
        steps_forklift += self.addCellsToPath_exit(current_cell, forklift)

        #   e verifica se o steps do forklift anterior é superior aos steps
        #       se for maior substitui e reseta os steps_forklift
        self.checkSteps(steps_forklift)


    def addCellsToPath_exit(self, current_cell, forklift):
        #vai encontrar o Pair igual ao current_cell to last_cell
        #e vai adicionar o array de cells ao self.all_path
        #e retorna os steps correspondentes
        last_cell = self.problem.agent_search.exit  # celula de saida
        for path in self.paths:
            if path == Pair(current_cell, last_cell):
                for i in range(len(path.cells)):
                    self.all_path[forklift].append(path.cells[i])
                return path.steps

    def addCellsToPath_product(self, current_cell, product_cell, forklift):
        #vai encontrar o Pair igual ao current_cell to product_cell
        #e vai adicionar o array de cells ao self.all_path
        #a ultima celula desse array nao vai adicionar,
        #mas vai adicionar uma nova celula Adjacente com os campos iguais a ultima celula do array e com a celula correpondente ao produto
        #e retorna os steps correspondentes
        for path in self.paths:
            if path == Pair(current_cell, product_cell):
                for i in range(len(path.cells) - 1):
                    self.all_path[forklift].append(path.cells[i])
                self.all_path[forklift].append(Adjancente(path.cells[len(path.cells) - 1], path.cell2))
                return path.steps

    # def addSteps(self, current_cell, destination_cell, forklift):
    #     for path in self.paths:
    #         if path == Pair(current_cell, destination_cell):
    #             return path.steps

    def checkSteps(self, steps):
        #vai ver se o nº de steps é maior que o self.steps
        #   se for vai substituir
        if self.steps < steps:
            self.steps = steps
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