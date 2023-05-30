
"""
@author: ghazaleh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd


##############################################################################
def read_file(file_name):
    vectors = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_columns = len(lines[0].split())
        for i in range(num_columns):
            vectors.append([])

        for line in lines:
            values = line.split()
            for i, value in enumerate(values):
                vectors[i].append((value))
    
    return vectors
##############################################################################

##############################################################################
def rpt_timing(file_name):
    
    counts_vector=read_file(file_name)
    
    rpt_time=[]
    for i in range(0,len(counts_vector[0])):
        rpt_time.append(i*10)
        
    return rpt_time

############################################################################## 

############################################################################## 
def robot_timing():
    
    time_robot= np.loadtxt("./time.txt")
    time=[]
    time_vector=[]
    for i in range(len(time_robot)):
        time.append(time_robot[i])
        
    for i in range (0,len(time)-1):      
        if (i % 2) == 0:
            average = (((time[i]+time[i+1])/2))
            time_vector.append((average*1000))

    
    return time_vector

############################################################################## 

############################################################################## 
def interpolation(file_name):
    
    counts_vector=read_file(file_name)
    x_time=rpt_timing(file_name)
    robot_time=robot_timing()
    interpolaited_counts_vector=[]
    for i in range(len(counts_vector)):
        f = interpolate.interp1d(x_time, counts_vector[i])
        y_new = f(robot_time)
        interpolaited_counts_vector.append(y_new)
        
        vector_length = len(interpolaited_counts_vector[0])
        with open("interpolaited_counts_all.txt", "w") as file:
            for i in range(vector_length):
                row = "\t".join(str(vector[i]) for vector in interpolaited_counts_vector)
                file.write(row + "\n")  
        

        


##############################################################################    
 
    
interpolation("denoised_counts_all.txt")




