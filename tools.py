import random

def get_bin_value(array_bin=[]):
    sum=0
    counter=0
    for i in range(-1,-len(array_bin)-1,-1):
        sum+=((2**counter)*array_bin[i])
        counter+=1

    return sum

def map_binary_value_to_domain(bin_num,domain_max,domain_min,bin_size):
    return (domain_min+((domain_max-domain_min)/((2**bin_size)-1)*bin_num))

def find_bits_for_accurct(max,min,accurcy):
    delta=(max-min)*(10**accurcy)
    counter=1
    while True:
        if (delta > 2**(counter-1)) and (delta<2**counter):
            break
        else:
            counter+=1

    return counter

def convert_binary_to_gray(array_bin=[]):
    gray=[]
    gray.append(array_bin[0])

    counter=1
    while counter!=(len(array_bin)):

        if (array_bin[counter]==1 and array_bin[counter-1]) or (array_bin[counter]==0 and array_bin[counter-1]==0):
            gray.append(0)
            counter+=1
        else:
            gray.append(1)
            counter+=1

    return gray


def conver_gray_to_binary(array_gray=[]):
    binary=[]
    binary.append(array_gray[0])
    counter=1
    while counter!=(len(array_gray)):
        if (array_gray[counter]==1 and binary[counter-1]==1) or (array_gray[counter]==0 and binary[counter-1]==0):
            binary.append(0)
            counter+=1
        else:
            binary.append(1)
            counter+=1

    return binary

def choice_zero_or_one():
    return random.randint(0,1)

def choice_int_between_a_and_b(a,b):
    return random.randint(a,b)

def choice_float_between_zero_and_one():
    return random.random()

def single_point_crossover(parent1,parent2):
    SizeOfParent=len(parent1)
    random_point=choice_int_between_a_and_b(0,SizeOfParent-1)
    child1=[0 for i in range(SizeOfParent)]
    child2=[0 for i in range(SizeOfParent)]
    child1[:random_point]=parent1[:random_point]
    child1[random_point:]=parent2[random_point:]
    child2[:random_point]=parent2[:random_point]
    child2[random_point:]=parent1[random_point:]
    return [child1,child2]

def calculate_roullet_wheel(chromosome_list):
    fitness_sum=0
    for fit in chromosome_list:
        fitness_sum+=fit.fitness
    rand_place_in_roullet=choice_int_between_a_and_b(a=0,b=int(fitness_sum))
    print(rand_place_in_roullet)

    choice_item=0
    for item in chromosome_list:
        choice_item+=item.fitness
        if choice_item>rand_place_in_roullet:
            return item.genes


def calculate_searching_space_accurcy(domain,bit_size):
    return (max(domain)-max(domain))/(2**bit_size)





