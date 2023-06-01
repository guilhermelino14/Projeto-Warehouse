from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        num_forklifts = len(ind1.problem.forklifts)
        cut1 = GeneticAlgorithm.rand.randint(0, num_forklifts)
        cut2 = GeneticAlgorithm.rand.randint(0, num_forklifts)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind1.genome)

        contains_child1 = []
        contains_child2 = []
        # ['2-2', '2-4', '1-3', '1-1']
        # ['1-2', '1-1', '2-3', '2-4']
        for i in range(cut1, cut2 + 1):
            child1[i] = ind1.genome[i]
            child2[i] = ind2.genome[i]
            contains_child1.append(ind1.genome[i][2])
            contains_child2.append(ind2.genome[i][2])



        j = cut2 + 1
        for i in range(cut2 + 1, num_genes):
            if not contains_child1.__contains__(ind2.genome[i][2]):
                child1[j] = ind2.genome[i]
                contains_child1.append(ind2.genome[i][2])
                j += 1

        if j == num_genes:
            j=0
        for i in range(cut2 + 1):
            if child1[j] != -1:
                break
            if not contains_child1.__contains__(ind2.genome[i][2]):
                child1[j] = ind2.genome[i]
                contains_child1.append(ind2.genome[i][2])
                j += 1
                if j == num_genes:
                    j = 0

        #child2
        j=cut2
        for i in range(cut2, num_genes):
            if not contains_child2.__contains__(ind1.genome[i][2]):
                child2[j] = ind1.genome[i]
                contains_child2.append(ind1.genome[i][2])
                j += 1
        if j == num_genes:
            j=0
        for i in range(cut2 + 1):
            if child2[j] != -1:
                break
            if not contains_child2.__contains__(ind1.genome[i][2]):
                child2[j] = ind1.genome[i]
                contains_child2.append(ind1.genome[i][2])
                j += 1
                if j == num_genes:
                    j = 0












        # é a recombinacao uniforme onde o nº de trocas vai ser 1/4 do nº de genes
        # mas em vez de trocar vai aplicar a recombinacao aritmetrica
        # pq os genes tem significado numerico, para ordenar
        # caso o gene 1 ser negativo e o do ind2 ser positivo alem de calcular os descendentes vao trocar de sinal
        # ex para os 3 genes que trocam: ind1[-3,9,-7] e ind2[-1,6,5] neste caso os descedentes vao ser
        #                           d1[-((3+1)/2), (9+6)/2, (7+5)/2] e d2[-((3+1)/2), (9+6)/2, -(7+5)/2]
        #                          d1[-1, 7, 6] d2[-1, 7, -6]


        # num_genes = ind1.num_genes
        # cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        # cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        # if cut2 < cut1:
        #     cut1, cut2 = cut2, cut1
        #
        # child1 = [0] * len(ind1.genome)
        # child2 = [0] * len(ind1.genome)
        #
        # contains_child1 = []
        # contains_child2 = []
        #
        # for i in range(cut1, cut2 + 1):
        #     contains_child1.append(abs(ind1.genome[i]))
        #     contains_child2.append(abs(ind2.genome[i]))
        #     if ind1.genome[i] > 0 and ind2.genome[i] < 0:
        #         child1[i] = -ind1.genome[i]
        #         child2[i] = ind2.genome[i]
        #         continue
        #     if ind1.genome[i] < 0 and ind2.genome[i] > 0:
        #         child1[i] = ind1.genome[i]
        #         child2[i] = -ind2.genome[i]
        #         continue
        #     # qd sao os ambos positivos ou negativos
        #     child1[i] = ind1.genome[i]
        #     child2[i] = ind2.genome[i]
        #
        # j = cut2+1
        # for i in range(cut2 + 1, num_genes):
        #     if not contains_child1.__contains__(abs(ind2.genome[i])):
        #         child1[j] = ind2.genome[i]
        #         contains_child1.append(abs(ind2.genome[i]))
        #         j += 1
        # if j == num_genes:
        #     j=0
        # for i in range(cut2 + 1):
        #     if child1[j] != 0:
        #         break
        #     if not contains_child1.__contains__(abs(ind2.genome[i])):
        #         child1[j] = ind2.genome[i]
        #         contains_child1.append(abs(ind2.genome[i]))
        #         j += 1
        #         if j == num_genes:
        #             j = 0
        #
        # #child2
        # j=cut2
        # for i in range(cut2 + 1, num_genes):
        #     if not contains_child2.__contains__(abs(ind1.genome[i])):
        #         child2[j] = ind1.genome[i]
        #         contains_child2.append(abs(ind1.genome[i]))
        #         j += 1
        # if j == num_genes:
        #     j=0
        # for i in range(cut2 + 1):
        #     if child2[j] != 0:
        #         break
        #     if not contains_child2.__contains__(abs(ind1.genome[i])):
        #         child2[j] = ind1.genome[i]
        #         contains_child2.append(abs(ind1.genome[i]))
        #         j += 1
        #         if j == num_genes:
        #             j = 0

        #problema que mete numeros iguais nos filhos
        #
        # for i in range((int)(num_genes/4)):
        #     swap_i = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        #     if ind1.genome[swap_i] > 0 and ind2.genome[swap_i] > 0:
        #         child1[swap_i] = child2[swap_i] = (int)(ind1.genome[i]*0.5 + ind2.genome[i]*0.5)
        #         continue
        #     if ind1.genome[swap_i] > 0 and ind2.genome[swap_i] < 0:
        #         child1[swap_i] = -(int)(ind1.genome[i]*0.5 + abs(ind2.genome[i])*0.5)
        #         child2[swap_i] = (int)(ind1.genome[i]*0.5 + abs(ind2.genome[i])*0.5)
        #         continue
        #     if ind1.genome[swap_i] < 0 and ind2.genome[swap_i] > 0:
        #         child1[swap_i] = (int)(abs(ind1.genome[i])*0.5 + ind2.genome[i]*0.5)
        #         child2[swap_i] = -(int)(abs(ind1.genome[i])*0.5 + ind2.genome[i]*0.5)
        #         continue
        #     child1[swap_i] = child2[swap_i] = (int)(abs(ind1.genome[i])*0.5 + abs(ind2.genome[i])*0.5)
        #
        # for i in range(num_genes):
        #     if child1[i] == 0:
        #         child1[i] = ind2.genome[i]
        #         child2[i] = ind1.genome[i]



        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
