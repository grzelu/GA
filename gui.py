# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:28:01 2018

@author: Michał
"""
import matplotlib.pyplot as plt
import time
import numpy as np
from cityx import city

#datax = [2,414,457,456,149,340,123,575,322,432,753,121,654,750]
#datay = [367,569,234,754,234,124,754,456,342,523,436,429,544,754]

#data_path = "C:\pyton\had12.txt"
#data_file = open(data_path,'r')

#datax = data_file.readline()
#datay = data_file.readline()
#datax = list(map(int,datax.split(',')))
#datay = list(map(int,datay.split(',')))
#print("Datax",datax)
#print("Datay",datay)
#cities = []

#print (datax[5])
#for i in range(0,len(datax)):
#    cities.append(city(datax[i],datay[i]))

#print('lencitites',len(cities))
    
def generateGraph(datax,datay):
    plt.axis([0, 800, 0, 800])
    plt.ylabel('some numbers')
    plt.plot(datax,
         datay,
         'ro')
    plt.show()
def drawLine(A,B):
    AX, AY = A.getXY()
    BX, BY = B.getXY()
    plt.plot([AX,BX],[AY,BY])
   # plt.show()
    
def calculateDistance(A,B):
    AX, AY = A.getXY()
    BX, BY = B.getXY()
    #print ("VALUES",BX,AX,BY,AY)
    distance = np.sqrt(abs((BX-AX))^2+abs((BY-AY))^2)
    return round(distance,2)



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
       flow_list.append(x)

data_file.close()



chr = [7, 9, 1, 2, 4, 8, 3, 5, 11, 0, 10, 6]
plt.axis([1, 800, 1, 800])

xxx = []
print('0000')
for i in city_list:
    xxx.append([i[1],i[2]])

for i in xxx:
    plt.plot(int(i[0]),int(i[1]),'ro')


for i in range(0,len(chr)-1):
    st = city_list[chr[i]]
    nd = city_list[chr[i+1]]
    plt.plot([int(st[1]),int(nd[1])],[int(st[2]),int(nd[2])],'k-')
    print ([st[1],st[2]],[nd[1],nd[2]])
    plt.draw()
    #plt.plot([st[1],st[2]],[nd[1],nd[2]])
    

plt.show()

    

