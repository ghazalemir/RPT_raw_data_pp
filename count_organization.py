"""
@author: ghazaleh
"""

import numpy as np
import pandas as pd


##############################################################################    
def read_counts(t,amp_id,sampling_time):
    #@ t is the total time of RPT sampling in minute
    #@ amp_id is amplidier id which shows in which order the RPT PC 
    #  write the data in the .txt file 
    #@ sampling_time shows the sampling time of the experiment in millisecond 
    
    #open the file
    count_reading= np.loadtxt("./Data.txt")
    
    #write the counts in a vector
    all_counts=[]
    for i in range(len(count_reading)):
        all_counts.append(count_reading[i])
    
    count=[]        
    time=int((t*60*1000)/sampling_time)
    for i in range (0,time):
        count.append(all_counts[7800+(i*26)+(amp_id-1)]) 
    return count
############################################################################## 


##############################################################################         
def write_count_all_det(amps_id_vector,t,sampling_time):
    #@ amps_id_vector contains the id number of amplifiers involved in the 
    #  experiment
    #@ t is the total time of the experiment, minute
    #@ sampling time is the interval of sampling, millisecond
    
    
    counts_vector=[]
    for i in range(len(amps_id_vector)):
        count=read_counts(t,amps_id_vector[i],sampling_time)
        counts_vector.append(count)
    
    vector_length = len(counts_vector[0])
    with open("counts_all.txt", "w") as file:
        for i in range(vector_length):
            row = "\t".join(str(vector[i]) for vector in counts_vector)
            file.write(row + "\n")           
############################################################################## 
        

##############################################################################       
#amps_id_vector=[6,8,17,20]
#t=250
#sampling_time=10      
#write_count_all_det(amps_id_vector,t, sampling_time)       
############################################################################## 

        
