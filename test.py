import unittest
from tools import convert_binary_to_gray
from tools import find_bits_for_accurct
from tools import conver_gray_to_binary
from tools import get_bin_value
# from GA import Chromosome
from GA import Genetic
from tools import calculate_searching_space_accurcy



class ToolTests(unittest.TestCase):

    def test_find_bits(self):
        max=2.5
        min=-1.5
        accur=3
        f=find_bits_for_accurct(max,min,accur)
        self.assertEqual(f,12)

    def test_convert_binary_to_gray(self):
        a=[1,0,1,0,0,1,0,1,0]
        gray=convert_binary_to_gray(array_bin=a)
        self.assertEqual(gray,[1,1,1,1,0,1,1,1,1])

    def test_convert_gray_to_binary(self):
        a=[1,1,1,1,0,1,1,1,1]
        binary=conver_gray_to_binary(array_gray=a)
        self.assertEqual(binary,[1,0,1,0,0,1,0,1,0])

    def test_both_convert_binary_and_gray(self):
        a = [1, 0, 1, 0, 0, 1, 0, 1,0,1,0,1,0,1,0,1,1,0]
        self.assertEqual(conver_gray_to_binary(array_gray=convert_binary_to_gray(array_bin=a)),a)

    def test_get_bin_value(self):
        a=[0,0,1,0,0]
        self.assertEqual(get_bin_value(a),4)

    # def test_map_value_to_domain(self):
    #     a=[0,1,1,0,1,1,1,0]
    #     bin_num=get_bin_value(array_bin=a)
    #     print(map_binary_value_to_domain(bin_num=bin_num,domain_max=20,domain_min=0,bin_size=len(a)))

    # def test_choice_zero_or_ine(self):
    #     print(choice_zero_or_one())
    # def test_probability(self):
    #     a=[12,13,45,98,78]
    #     self.assertEqual(calculate_probability(12,fitness_list=a),0.048)

    # def test_choice_roullet(self):
    #     a=[12,45,152,32,65,89,78,15]
    #     b=calculate_roullet_wheel(fitness_list=a)
    #     print(b)

    # def test_chromosome(self):
    #     obj=Chromosome()
    #     obj.create_randomization_genes(num_of_genes=12)
    #     print(obj.genes)
    #     print(obj.get_chromosome_value())
    #     print(obj.get_gray_code())

    def test_genetic_algirithm(self):
        def function(x):
            return (x-2)**2
        def fitness_function(x):
            return function(x)
        domain=[-1,5]

        genetic=Genetic()
        genetic.number_of_papulation=12
        genetic.function=function
        genetic.fitness_function=fitness_function
        genetic.accurcy=1
        genetic.end_condition_cost=100
        genetic.domain=domain
        val_list=[]
        for item in genetic.main():
           val_list.append(item.get_chromosome_value())
        print(val_list)
        print(calculate_searching_space_accurcy(domain=domain,bit_size=find_bits_for_accurct(max=max(domain),min=min(domain),accurcy=1)))
if __name__=="__main__":
    unittest.main()
