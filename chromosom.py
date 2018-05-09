# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:35:45 2018

@author: Michał
"""
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
       flow_list.append(line.split(','))

list_of_cities = cities(flow = flow_list,cities=city_list)
for i in range(0,len(city_list)):
    list_of_cities.append(city(city_list[i]))



def calculateDistance(A,B):
    Bx = int(B.x)
    By = int(B.y)
    Ax = int(A.x)
    Ay = int(A.y)
    distance = np.sqrt((Bx-Ax)**2+(By-Ay)**2)
    return float(round(distance,2))

def getFlowScore(cityA, cityB):
    print (cityA,cityB)
    cityAnumber = cities.search(cityA.name)
    cityBnumber = cities.search(cityB.name)
    return flow_matrix[cityAnumber,cityBnumber]
class chromosome():   
    def __init__(self,chromosome_size):
        self.gene_list = []
        self.fitness = 0
        self.n_fitness=0
        temp_city = list_of_cities[1:-1]
        random.shuffle(temp_city)
        self.gene_list.append(list_of_cities[0])
        while True:
            #time.sleep(1)
            for _city in temp_city:
                self.gene_list.append(_city)
                if (len(self.gene_list)==chromosome_size-1):
                    #print (self.gene_list)
                    break

            break
            
        self.gene_list.append(list_of_cities[-1])
        
    def calculate_fitness(self):
        score = 0
        dd=0
        ff=0
        for idx in range (0, len(self.gene_list)):
            if (self.gene_list[idx+1]==self.gene_list[-1]):
                break
            _distanceScore = calculateDistance(self.gene_list[idx],self.gene_list[idx+1])
            _flowScore = float(list_of_cities.getFlowValue(self.gene_list[idx],self.gene_list[idx+1]))*10
            dd+=_distanceScore
            ff+=_flowScore
        
        self.fitness = 1/dd*ff
        return self.fitness

def _crossover(_ch1,_ch2,idx):
        ch1, ch2 = copy.copy(_ch1), copy.copy(_ch2)
        #print ("1zmiana {} z {}".format(ch1.gene_list,ch2.gene_list))
        #print ("ORYGINAL {} z {}".format(_ch1.gene_list,_ch2.gene_list))
        for i in idx:
            ch1gene = ch1.gene_list[i]
            ch2gene = ch2.gene_list[i]
            ch1.gene_list[i] = ch2gene
            ch2.gene_list[i] = ch1gene
        return ch1,ch2       

class population:
    def __init__(self,population_size=100,chromosome_size = len(list_of_cities),generate = True):
        self.population_list = []
        self.chromosome_size = chromosome_size  
        for i in range(0,population_size):
            self.population_list.append(chromosome(chromosome_size))
        if generate == False:
            counter = 1
            for chr in self.population_list:
                #print ("Z",chr.gene_list)
                for gene_idx in range(1,len(chr.gene_list)-1):
                    counter+=1
                    #print ("Z",allele)
                    chr.gene_list[gene_idx]=list_of_cities[counter]
                    #print("NA",allele)
                    if counter == len(list_of_cities)-2:
                        counter=1
                #print ("N",chr.gene_list)
                    
    def calculateFitness(self):
        fitness=0
        for chr in self.population_list:
            fitness += chr.calculate_fitness()
        self.whole_fitness = fitness
        testscore = 0
        for chr in self.population_list:
            chr.n_fitness = chr.fitness/self.whole_fitness

    def selection(self,elitism = False):
        #from operator import itemgetter
        #new_generation= [] 
        #
        #print("selected gene")
        #print (self.population_list[0].fitness)
        #self.population_list.sort(key=lambda x:x.fitness, reverse = True)
        #print("after gene")
        #print (self.population_list[0].fitness)
        #for i in range(0,round(len(self.population_list)*0.3)):
        #    new_generation.append(self.population_list.pop(0))
        #for i in new_generation:
        #    print(i.fitness)
        new_generation = []
        #print(len(self.population_list))
       
        for i in range(0,len(self.population_list)-1 if elitism  else len(self.population_list) ):
            rint = random.randint(0,len(self.population_list)-1)
            rint2 = random.randint(0,len(self.population_list)-1)
            #print (rint,rint2)
            first_parent_idx = rint
            second_parent_idx = rint2
            if self.population_list[first_parent_idx].fitness > self.population_list[second_parent_idx].fitness:
                winner = self.population_list[first_parent_idx]
            else:
                winner = self.population_list[second_parent_idx]
            new_generation.append(winner)
        temp = copy.copy(self.population_list)
        temp.sort(key=lambda x:x.fitness, reverse = True)
        #print(temp[0].fitness)
        new_generation.append(temp[0])
        self.new_generation = new_generation
        #if len(new_generation)<len(self.population_list):
        #    new_generation.append(self.population_list[np.argmax('fitness')])
       # new_generation.append(self.population_list[np.argmax('fitness')])
    def _crossover(self,_ch1,_ch2,idx):
        ch1, ch2 = copy.copy(_ch1), copy.copy(_ch2)
        #print ("1zmiana {} z {}".format(ch1.gene_list,ch2.gene_list))
        #print ("ORYGINAL {} z {}".format(_ch1.gene_list,_ch2.gene_list))
        for i in idx:
            ch1gene = ch1.gene_list[i]
            ch2gene = ch2.gene_list[i]
            ch1.gene_list[i] = ch2gene
            ch2.gene_list[i] = ch1gene
        return ch1,ch2       
    def crossover(self,crossover_probability,ng=[],not_cross=[]):
        ng_chr = ng
        not_cross=not_cross
        if not ng_chr:
            ng_chr = self.new_generation
        #ng_chr =self.new_generation
        chr_to_crossover = []
        chr_unchanged = []
        for chr in ng_chr:
            if crossover_probability > random.uniform(0,1):
                chr_to_crossover.append(copy.deepcopy(chr))
            else:
                chr_unchanged.append(copy.deepcopy(chr))
        #print(chr_to_crossover)
        #print(chr_unchanged)
        enumList = list(enumerate(chr_to_crossover))
        crossover_tuples = []  
        after_change = []
        while enumList:
            en_chr_idx, c_chrom = enumList.pop()
            if not enumList:
                chr_unchanged.append(c_chrom)
                break
            cb_idx, cross_buddy = random.choice(enumList)
            enumList = [(x_k, x_v) for x_k, x_v in enumList if x_k != cb_idx]
            crossover_tuples.append((c_chrom, cross_buddy))
            
        for chr in crossover_tuples:
            n_cities_to_change = random.randint(1,self.chromosome_size-2)
            #print (n_cities_to_change)
            idx_to_change=[]
            for i in range(0,n_cities_to_change):
                idx_to_change.append(random.randint(1,self.chromosome_size-2))
            idx_to_change = set (idx_to_change)
            #print (idx_to_change)
            #print(chr[0].gene_list,chr[1].gene_list)
            cchr1,cchr2 = _crossover(chr[0],chr[1],idx_to_change)
            #print(chr[0].gene_list,chr[1].gene_list)
            #print(cchr1.gene_list,cchr1.gene_list)
            #print('-----------')
            after_change.append(cchr1)
            after_change.append(cchr2)
            
        self.new_generation = after_change + chr_unchanged + not_cross
        return self.new_generation

        
        
        
        
        