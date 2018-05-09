# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:21:35 2018

@author: grzej
"""
from gui import calculateDistance
from cityx import city,cities
import numpy as np
import random,copy

data_path = "DATAtt.txt"
data_file = open(data_path,'r')
city_list = []
flow_list = [] 
flow=False
while True:
    line = data_file.readline().strip('\r\n')
    if line=='END':
        data_file.close()
        break  
    if (line=='---'):
        flow=True
        continue
    elif(flow==False):
       city_list.append(line.split(','))

    if (flow==True):
        
       
       x=line.split(',')
       print(type(line.split(',')))
       flow_list.append(x)

data_file.close()

list_of_cities = cities(flow = flow_list,cities=city_list)
data_path = "DATA_xd.txt"
data_matrix = np.loadtxt(data_path,skiprows=13)
flow_matrix = data_matrix
#print (flow_matrix)
for i in range(0,len(city_list)):
    list_of_cities.append(city(city_list[i]))
    
print (list_of_cities)



def generate_random_population(n_cities, n_chromosomes):
    population_list = []
    for ch_idx in range(n_chromosomes):
        rand_chromosome = list(range(0, n_cities))
        random.shuffle(rand_chromosome)
        population_list.append(rand_chromosome)
    return population_list

x= generate_random_population(5,10)

def generate_distance_matrix(list_of_cities):
    size = len(list_of_cities)
    xxx = np.zeros((size,size))
    for y in range(0,len(list_of_cities)):
        for x in range(0,len(list_of_cities)):
           # print(x,y,list_of_cities[x],list_of_cities[y])
            xxx[x][y]=calculateDistance(list_of_cities[x],list_of_cities[y])
    return xxx       
    #print(xxx)
distance_matrix = generate_distance_matrix(list_of_cities)
print(type(distance_matrix),type(flow_list))
def fitness_score(population_list, flow_matrix, distance_matrix):
    n_facilities = len(population_list[0])
    fitness_scores_list = []
    for chromosome_list in population_list:
        chromosome_fitness = 0
       # print("E",chromosome_list)
        tot_dst=0
        tot_flw=0
        for i in range(0,len(chromosome_list)-1):
            st_idx = chromosome_list[i]
            nd_idx = chromosome_list[i+1]
            dst = distance_matrix[st_idx][nd_idx]
            flw = flow_matrix[st_idx][nd_idx]
            tot_dst+=dst
            tot_flw+=flw
        chromosome_fitness = tot_dst*tot_flw
        
        
        
        fitness_scores_list.append(1. / (chromosome_fitness / 2.))
    return fitness_scores_list

#print(1. / fitness_score(x, flow_matrix, distance_matrix)[0])
#fitness_score(x, flow_matrix, distance_matrix)
def normalise_fitness_score(fitness_score):
    return np.array(fitness_score) / np.sum(fitness_score)

def tournament_selection(population_list, fitness_scores_list, elitism=True):
    # Create new population
    new_species = []
    population_size = len(fitness_scores_list)
    population_size = population_size - 1 if elitism else population_size
    for _ in range(0, population_size):
        # Take best
        of_parent_idx = random.randint(0, len(fitness_scores_list) - 1)
        tf_parent_idx = random.randint(0, len(fitness_scores_list) - 1)
        if fitness_scores_list[of_parent_idx] > fitness_scores_list[tf_parent_idx]:
            ch_winner = population_list[of_parent_idx]
        else:
            ch_winner = population_list[tf_parent_idx]
        new_species.append(ch_winner)
    new_species.append(population_list[np.argmax(fitness_scores_list)])
    return new_species

def chromosome_crossover(chromosome_o, chromosome_s):
    # Random point to crossover
    chr_o, chr_s = copy.copy(chromosome_o), copy.copy(chromosome_s)
    pos = random.randint(0, len(chromosome_o) - 1)

    # Change chromosome
    for ch_idx in range(0, pos):
        # values on ind
        fac_o = chr_o[ch_idx]
        fac_s = chr_s[ch_idx]
        
        # Values for swap
        fac_os_idx = chr_o.index(fac_s)
        fac_so_idx = chr_s.index(fac_o)
        
        # Save values
        chr_o[fac_os_idx] = fac_o
        chr_s[fac_so_idx] = fac_s
        
        # Change values
        chr_o[ch_idx] = fac_s
        chr_s[ch_idx] = fac_o
    return chr_o, chr_s

def crossover_population(new_species, crossover_probability):
    # Select for crossover
    species_nc = []
    crossover_list = []
    for n_chrom in new_species:
        rnd = random.uniform(0, 1)
        if rnd < crossover_probability:
            crossover_list.append(n_chrom)
        else:
            species_nc.append(n_chrom)
            
    crossover_tuples = []    
    # Create crossover buddies
    cr_iterate = list(enumerate(crossover_list))
    while cr_iterate:
        cch_idx, c_chrom = cr_iterate.pop()
        if not cr_iterate:
            species_nc.append(c_chrom)
            break
        cb_idx, cross_buddy = random.choice(cr_iterate)
        cr_iterate = [(x_k, x_v) for x_k, x_v in cr_iterate if x_k != cb_idx]
        crossover_tuples.append((c_chrom, cross_buddy))

    # Crossover to list
    after_cover = []
    for cr_tup in crossover_tuples:
        cr_o, cr_t = chromosome_crossover(cr_tup[0], cr_tup[1])
        after_cover.append(cr_o)
        after_cover.append(cr_t)

    # New population
    new_species = after_cover + species_nc
    return new_species

def mutation_population(new_species, mutation_probability):
    # # MUTATION
    mutated = []
    for chromosome in new_species:
        for b_idx in range(0, len(chromosome)):
            rnd = random.uniform(0, 1)
            if rnd < mutation_probability:
                swap_idx = random.randint(0, len(chromosome) - 1)
                old_mut_val = chromosome[b_idx]
                chromosome[b_idx] = chromosome[swap_idx]
                chromosome[swap_idx] = old_mut_val
        mutated.append(chromosome)
    return mutated
population_list = generate_random_population(12, 1000)
crossover_probability=0.8
mutation_probability=0.008
for epoch in range(0, 100000):
    fit_scores = fitness_score(population_list, flow_matrix, distance_matrix)
    fit_scores_norm = normalise_fitness_score(fit_scores)
    selected_ch = tournament_selection(population_list, fit_scores_norm, elitism=False)
    crossed_ch = crossover_population(selected_ch, crossover_probability)
    mutated_ch = mutation_population(crossed_ch, mutation_probability)
    max_fitness = np.max(fit_scores)
    max_chromosome = population_list[np.argmax(fit_scores)]
    print("Epoch: {}, Population fitness score: {}, Max score: {}, Max chromosome: {}".format(epoch, 1. / np.mean(fit_scores), 
                                                                                              1. / max_fitness, max_chromosome))
    population_list = crossed_ch
