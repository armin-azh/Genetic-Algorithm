import math

def linear_scaling(func,a,b):
    return a*func+b

def dynamic_linear_scaling(func,a,b,t):
    return a*func+b*t

def pow_scaling(func,a):
    return func*a

def logarithm_scaling(func,b):
    return b-math.log10(func)

def nomalization(fitness_list,func,y):
    f_max=max(fitness_list)
    f_min=min(fitness_list)
    return (f_max-func+y)/(f_max-f_min+y)
