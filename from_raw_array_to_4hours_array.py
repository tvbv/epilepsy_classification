#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:22:20 2022

@author: thomas
"""
import numpy as np
import matplotlib.pyplot as plt

for number_of_patient in [1,2,3,5,6,7,8,9,10,11,14,16,20,21,22,23,24]:
    
    x = np.load('/data/thomas/classification epilepsy/chb-mit-scalp-eeg-database-1.0.0/dataset/'+ 'temporel'+str(number_of_patient)+'_x.npy') 
    y = np.load('/data/thomas/classification epilepsy/chb-mit-scalp-eeg-database-1.0.0/dataset/'+ 'temporel'+str(number_of_patient)+'_y.npy') 
    
    acc = 0
    y[:,1] = y[:,1]/1000
    y_new = np.zeros(y.shape[0])
    for i in range(y.shape[0]-1):
        y_new[i] = acc + y[i,1]
        if y[i+1,1]==0.0:
            #print(i,y[i-1,1])
            acc += y[i,1]
    y_new[-1] = acc + y[-1,1]
    plt.plot(np.arange(0,y.shape[0],1),y_new)
    
    
    y_interictal = np.ones(y_new.shape)
    memoire_interictal = 0
    flag_effet_de_bord = 0
    for i in range(len(y[:,1])-1):
        if y[i,0] == 1 and y[i+1,0]==0 :
            memoire_interictal = i
            flag_effet_de_bord = 1
        if (y_new[i] < y_new[memoire_interictal]+4*3600 or y[i,0]==1 )and flag_effet_de_bord:
            y_interictal[i]=0
            
            
    memoire_interictal = -1
    flag_effet_de_bord = 0
    for i in range(len(y[:,1])-1,0,-1):
            if y[i,0] == 1 and y[i-1,0]==0 :
                memoire_interictal = i
                flag_effet_de_bord = 1
            if (y_new[i] > y_new[memoire_interictal]-4*3600 or y[i,0]==1 )and flag_effet_de_bord:
                y_interictal[i]=0
    plt.plot(np.arange(0,y.shape[0],1),y_interictal*y_new[-1],'r')
    plt.show()  
    print(sum(y_interictal),sum(y[:,0]))
    
    x_to_save = []
    y_to_save = []
    
    for i in range(y.shape[0]):
        if y[i,0] == 1:
            x_to_save.append(x[i])
            y_to_save.append(1)
        elif y_interictal[i]==1:
            x_to_save.append(x[i])
            y_to_save.append(0)
    np.save('/data/thomas/classification epilepsy/chb-mit-scalp-eeg-database-1.0.0/dataset/4hours/'+ 'temporel'+str(number_of_patient)+'_x_4hours.npy',np.float16(np.array(x_to_save)))
    np.save('/data/thomas/classification epilepsy/chb-mit-scalp-eeg-database-1.0.0/dataset/4hours/'+ 'temporel'+str(number_of_patient)+'_y_4hours.npy',np.array(y_to_save))
            