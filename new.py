import copy
import random,time
import numpy as np
import matplotlib.pyplot as plt
#import gui
from chromosom import *
from gui import calculateDistance,generateGraph
from cityx import city,cities as cti

crossover_probability = 0.8
mutation_probability = 0.08


#Generate random population
populacja = population(10,8,generate=False)
populacja.calculateFitness()
#populacja_bkp = populacja
for i in populacja.population_list:
    print (i.gene_list,i.fitness)
best = 0
best_chr=[]
#for i in range(0,100):
#    populacja.calculateFitness()
#    populacja.selection(elitism=False)
#    populacja.crossover(crossover_probability)
#    temp = copy.deepcopy(populacja)
#    temp.population_list.sort(key=lambda x:x.fitness, reverse = True)
#    if temp.population_list[0].n_fitness < best:
#        best = temp.population_list[0].n_fitness
#        best_chr = temp.population_list[0].gene_list
#        
#    print ("BEST Fitness {} {}, best in generation {} {}".format(best,best_chr,temp.population_list[0].fitness,temp.population_list[0].gene_list))
#    populacja.population_list = populacja.new_generation
    #for i in populacja.population_list:
    #    print (i.gene_list,i.fitness)
    #for i in populacja.population_list:
    #    print (i.gene_list,i.fitness)

    #print('ORYGINAL')
    #for i in populacja_bkp.population_list:
    #    print (i.gene_list,i.fitness)
    #print('ZMIENIONE')
    #for i in populacja.population_list:
    #    print (i.gene_list,i.fitness)
    #print('posortowenae') 
    #temp = copy.deepcopy(populacja)
    #temp.population_list.sort(key=lambda x:x.fitness, reverse = True)
    #for i in populacja.population_list:
    #    print (i.gene_list,i.fitness)
    #print('Nowa generacja') 
    #populacja.crossover(crossover_probability)   
    #for i in populacja.new_generation:
    #    print (i.gene_list,i.fitness)