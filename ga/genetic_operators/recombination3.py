from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # [1, 3, |0, 2, 5, 4, 0, 8, 7, 6]
        # [2, 1, 3, |0, 6, 0, 7, 4, 5, 6]
        last_product = len(ind1.problem.products)  # os separadores sao depois do ultimo produto
        num_genes = ind1.num_genes
        num_forklifts = len(ind1.problem.forklifts)
        if num_forklifts == 1:
            cut1_ind1 = cut1_ind2 = 0
            cut2_ind1 = cut2_ind2 = num_genes-1
            count_seperator_child1 = count_seperator_child2 = 0
        else:
            forkliftToRecombine = GeneticAlgorithm.rand.randint(1, num_forklifts)
            cut1_ind1, cut2_ind1, count_seperator_child1, separador_child1 = self.computeCuts(ind1, forkliftToRecombine)
            cut1_ind2, cut2_ind2, count_seperator_child2, separador_child2 = self.computeCuts(ind2, forkliftToRecombine)




        child1 = [-1] * num_genes
        for i in range(cut1_ind1, cut2_ind1+1):
            child1[i] = ind1.genome[i]

        #i é o indice do child
        #j é o indice do ind
        j = cut2_ind2
        j = self.avancarIndiceNumChromossomo(j, num_genes)
        for i in range(cut2_ind1+1, num_genes):
            if child1[i] == -1:
                while child1.__contains__(ind2.genome[j]):
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                if ind2.genome[j] > last_product and count_seperator_child1 < num_forklifts - 1:
                    separador_child1 += 1
                    if separador_child1 > num_genes:
                        separador_child1 = last_product + 1
                    child1[i] = separador_child1

                    count_seperator_child1 += 1
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                    continue
                child1[i] = ind2.genome[j]

        for i in range(cut1_ind1):
            if child1[i] == -1:
                while child1.__contains__(ind2.genome[j]):
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                if ind2.genome[j] > last_product and count_seperator_child1 < num_forklifts - 1:
                    # se for um separador #e se ainda preencheu todos os separadores
                    # vai prencher com um separador
                    separador_child1 += 1
                    if separador_child1 > num_genes:
                        separador_child1 = last_product + 1
                    child1[i] = separador_child1

                    count_seperator_child1 += 1
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                    continue
                child1[i] = ind2.genome[j]

        237
        child2 = [-1] * num_genes
        for i in range(cut1_ind2, cut2_ind2+1):
            child2[i] = ind2.genome[i]

        j = self.avancarIndiceNumChromossomo(j, num_genes)
        for i in range(cut2_ind2+1, num_genes):
            if child2[i] == -1:
                while child2.__contains__(ind1.genome[j]):
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                if ind1.genome[j] > last_product and count_seperator_child2 < num_forklifts - 1:
                    separador_child2 += 1
                    if separador_child2 > num_genes:
                        separador_child2 = last_product + 1
                    child2[i] = separador_child2

                    count_seperator_child2 += 1
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                    continue
                child2[i] = ind1.genome[j]
        for i in range(cut1_ind2):
            if child2[i] == -1:
                while child2.__contains__(ind1.genome[j]):
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                if ind1.genome[j] > last_product and count_seperator_child2 < num_forklifts - 1:
                    separador_child2 += 1
                    if separador_child2 > num_genes:
                        separador_child2 = last_product + 1
                    child2[i] = separador_child2

                    count_seperator_child2 += 1
                    j = self.avancarIndiceNumChromossomo(j, num_genes)
                    continue
                child2[i] = ind1.genome[j]




        ind1.genome = child2
        ind2.genome = child1

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"

    def computeCuts(self, ind : Individual, forkliftToRecombine):
        last_product = len(ind.problem.products) # os last_productes sao depois do ultimo produto
        if forkliftToRecombine == 1:
            for i in range(len(ind.genome)):
                if ind.genome[i] > last_product:
                    return 0, i, 1, ind.genome[i]
            return 0, ind.num_genes - 1, 1, ind.genome[ind.num_genes - 1]

        count = 1 #forklift count
        for i in range(len(ind.genome)):
            if ind.genome[i] > last_product:
                count += 1
                if count == forkliftToRecombine:
                    cut1 = i

        for i in range(cut1+1, len(ind.genome)):
            if ind.genome[i] > last_product:
                return cut1, i, 2, ind.genome[i]
        return cut1, ind.num_genes - 1, 1, ind.genome[cut1]


    def avancarIndiceNumChromossomo(self, i, num_genes):
        return i+1 if i+1 != num_genes else 0