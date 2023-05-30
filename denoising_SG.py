"""
@author: ghazaleh
"""


import numpy as np
from scipy.signal import savgol_filter


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
def Savitzky_Golay(file_name,window_length,polyorder):
    
    denoised_count_vector=[]
    counts_vector=read_file(file_name)
    for i in range (len(counts_vector)):
        denoised_count= savgol_filter(counts_vector[i], 
                                      window_length, polyorder)
        denoised_count_vector.append(denoised_count)
        
    
    vector_length = len(denoised_count_vector[0])
    with open("denoised_counts_all.txt", "w") as file:
        for i in range(vector_length):
            row = "\t".join(str(vector[i]) for vector in denoised_count_vector)
            file.write(row + "\n")  
    
       
##############################################################################

   
window_length=301
polyorder=1
Savitzky_Golay("shifted_counts_all.txt",window_length,polyorder)