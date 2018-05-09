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
    if ((BX-AX)^2+(BY-AY)^2<0):
        return 0
    else:
        distance = np.sqrt((BX-AX)^2+(BY-AY)^2)
        return round(distance,2)









