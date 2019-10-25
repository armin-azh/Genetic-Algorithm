from tools import choice_zero_or_one
from tools import choice_int_between_a_and_b
from tools import choice_float_between_zero_and_one
from tools import get_bin_value
from tools import convert_binary_to_gray
from tools import single_point_crossover
from tools import find_bits_for_accurct
from tools import calculate_roullet_wheel
from tools import map_binary_value_to_domain

class Chromosome:
    def __init__(self):
        self.genes=[]
        self.fitness=None

    def update_fitness(self,value,domain):
        self.fitness=map_binary_value_to_domain(bin_num=value,domain_max=max(domain),domain_min=min(domain),bin_size=len(self.genes))

    def update_genes(self,value_list):
        self.genes=value_list

    def create_randomization_genes(self,num_of_genes):
        try:
            for i in range(num_of_genes):
                self.genes.append(choice_zero_or_one())
        except:
            ValueError('you were in the invalid number of genes')

    def get_chromosome_value(self):
        return get_bin_value(self.genes)

    def get_gray_code(self):
        return convert_binary_to_gray(self.genes)


class Generation:
    def __init__(self):
        self.generate_number=None
        self.members=[]

    def __str__(self):
        return 'Generation number ({})'.format(self.generate_number)

    def add_chromosome_to(self,chromo_obj=None):
        self.members.append(chromo_obj)


class Genetic:
    def __init__(self,function_name=None,fitness_function_name=None,domain=None,papulate_num=None):
        self.number_of_papulation = papulate_num
        self.papulation = []
        self.function = function_name
        self.fitness_function = fitness_function_name
        self.domain = domain
        self.mutation_rate = 0
        self.crossover_rate = 1
        self.mutation_bit = 1
        self.end_condition_cost = None
        self.accurcy = 1
        self.genes_num = None

    def _add_generation_to_papulation(self,generation_obj=Generation()):
        generation_obj.generate_number=len(self.papulation)+1
        self.papulation.append(generation_obj)

    def _crossover_check(self):
        if self.crossover_rate > choice_float_between_zero_and_one():
            return True
        else:
            return False

    def _crossover(self,parent1,parent2):
        children=single_point_crossover(parent1=parent1,parent2=parent2)
        return children

    def _mutation_check(self):
        if self.mutation_rate >= choice_float_between_zero_and_one():
            return True
        else:
            return False

    def _mutation(self,gene=[]):
        for i in range(self.mutation_bit):
            random_place=choice_int_between_a_and_b(a=0,b=len(gene)-1)
            replace_random_bit=choice_zero_or_one()
            gene[random_place]=replace_random_bit
        return gene

    def _last_papulation(self):
        try:
            return self.papulation[-1]

        except:
            raise ValueError('the papulation list is empty')

    def main(self):
        self.genes_num=find_bits_for_accurct(max=max(self.domain),min=min(self.domain),accurcy=self.accurcy)
        first_generation=Generation()
        for i in range(self.number_of_papulation):
            new_chromosome=Chromosome()
            new_chromosome.create_randomization_genes(num_of_genes=self.genes_num)#1)initial papulation
            fitness=self.fitness_function(new_chromosome.get_chromosome_value())
            new_chromosome.update_fitness(fitness,domain=self.domain)
            first_generation.add_chromosome_to(new_chromosome)

        self._add_generation_to_papulation(first_generation)

        counter=self.end_condition_cost

        while counter != 0:
            generation=self._last_papulation()
            next_generation=Generation()
            # next_generation.generate_number=generation_index

            for i in range(int(self.number_of_papulation/2)):
                members=generation.members

                if self._crossover_check():
                    parent1=calculate_roullet_wheel(members)
                    parent2=calculate_roullet_wheel(members)

                    childrens=self._crossover(parent1=parent1,parent2=parent2)
                    final_children=[]
                    for child in childrens:
                        if self._mutation_check():
                            final_children.append(self._mutation(gene=child))
                        else:
                            final_children.append(child)

                    del childrens
                    child1=Chromosome()
                    child1.genes=final_children[0]
                    child1.update_fitness(value=self.fitness_function(child1.get_chromosome_value()),domain=self.domain)
                    child2=Chromosome()
                    child2.genes=final_children[1]
                    child2.update_fitness(value=self.fitness_function(child2.get_chromosome_value()),domain=self.domain)
                    next_generation.add_chromosome_to(child1)
                    next_generation.add_chromosome_to(child2)

            if (self.number_of_papulation-len(next_generation.members)) > 0:
                delta = self.number_of_papulation - len(next_generation.members)

                for i in range(delta):
                    chro = Chromosome()
                    chro.update_genes(calculate_roullet_wheel(generation.members))
                    chro.update_fitness(value=self.fitness_function(chro.get_chromosome_value()),domain=self.domain)
                    next_generation.add_chromosome_to(chro)
            self._add_generation_to_papulation(next_generation)
            counter-=1


        new_list = self.papulation[-1].members
        return new_list