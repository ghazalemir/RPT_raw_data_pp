
"""
@author: ghazaleh
"""

import numpy as np

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
def write_synchronized_data(file_name,time,sampling_time,lag):
    #@ file_name is the name of file which contains the recorded counts 
    #  from all the detectors
    #@ time is the total time of the experiment, minute
    #@ sampling time is the interval of sampling, millisecond
    #@ lag is the amount of calculated time for the lag between the RPT start
    #  point and the robot start point
    
    
    counts_vector=read_file(file_name)

    last_sampling_time= int ((time*60*1000)/sampling_time)
    print(last_sampling_time)
    useless_data=int((lag*1000)/sampling_time)
    shifted_count=[]
    for i in range(len(counts_vector)):
        new_count=[]
        for j in range(useless_data,last_sampling_time):
            new_count.append(counts_vector[i][j])
        shifted_count.append(new_count)
        
    
    vector_length = len(shifted_count[0])
    with open("shifted_counts_all.txt", "w") as file:
        for i in range(vector_length):
            row = "\t".join(str(vector[i]) for vector in shifted_count)
            file.write(row + "\n")  
                
##############################################################################   

file_name="counts_all.txt"
time=250
sampling_time=10
lag=12.8
write_synchronized_data(file_name,time,sampling_time,lag)




