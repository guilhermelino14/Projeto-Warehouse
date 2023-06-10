from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # troca o gene do produto com um gene de forklift
        num_genes = len(ind.genome)
        num_forklifts = len(ind.problem.forklifts)

        print("BEFORE" + str(ind.genome))
        # Encontra o indice do forklift com menos produtos
        if num_forklifts > 1:
            count_products = 0
            less_products = num_genes
            last_product = len(ind.problem.products)  # os separadores sao depois do ultimo produto
            separator_small_forklift = last_separator_i = 0
            for i in range(num_genes):
                if ind.genome[i] > last_product:
                    if count_products < less_products:
                        less_products = count_products
                        separator_small_forklift = i
                    count_products = 0
                    last_separator_i = i
                    continue
                count_products += 1
            # ao terminar o for faz a verificacao pq o ultimo forklift acaba sem separador
            # mas ao inves de defenir o separador usa o anterior para aumentar os seus produtos
            if count_products <= less_products:
                aux = ind.genome[last_separator_i]
                ind.genome[last_separator_i] = ind.genome[last_separator_i-1]
                ind.genome[last_separator_i-1] = aux
            #se nao vai aumentar sempre para a frente
            else:
                aux = ind.genome[separator_small_forklift]
                ind.genome[separator_small_forklift] = ind.genome[separator_small_forklift + 1]
                ind.genome[separator_small_forklift + 1] = aux

            print("AFTER " + str(ind.genome))




    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
