
"""
@author: ghazaleh
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from scipy import signal

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#To achieve synchronization, we employ a single detector where we move 
#the particle towards it, perpendicular to the detector's face,
# and subsequently retract it.
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

##############################################################################
def read_count():
    
    #read the count number of the detector that we used for synchronization
    count_reading= np.loadtxt("./handshake_det.txt")   
    count=[]
    
    for i in range(len(count_reading)):
        count.append(count_reading[i])
    
    return count
##############################################################################    
    

##############################################################################
def cross_correlation(time,sampling_time,index):
    #@ time must be minimum the duration of the particle round movement 
    #  in front of the detector in seconds
    #@ sampling time is the interval of time to record the count
    #@ index represents the number of data points recorded by the robot for 
    #  TCP position during a single back-and-forth movement 
    #  to achieve synchronization.
    
    count=read_count()   
    count_first_cycle=[]     
    for i in range (0,int(time/sampling_time)):
        count_first_cycle.append(count[i])
        
    
    #normalizing the counts to visualize it better with the position data
    normalized_count = (count_first_cycle-np.min(count_first_cycle))/(np.max(count_first_cycle)-np.min(count_first_cycle)) 
    #read the data of TCP position from the robot
    df = pd.read_csv("x_y_robot_position.txt", sep=",")
    pos_x=[]
    
    for i in range(index):
        pos_x.append(df.iat[i, 0]-df.iat[0,0])

    normalized_pos = (pos_x - np.min(pos_x)) / (np.max(pos_x) - np.min(pos_x))  

    #performing the cross correlation
    count_np = np.array(normalized_count)
    pos_x_np= np.array(normalized_pos)
    correlation = np.correlate(count_np, pos_x_np, mode='full')  
    lags = signal.correlation_lags(count_np.size, pos_x_np.size, mode="same")
    lag = lags[np.argmax(correlation)]
    print(lag)
    return lag

##############################################################################   

##############################################################################
def visualisation(time,sampling_time,index):
    count=read_count()   
    count_first_cycle=[]     
    for i in range (0,int(time/sampling_time)):
        count_first_cycle.append(count[i])
        
    
    #normalizing the counts to visualize 
    normalized_count = (count_first_cycle - np.min(count_first_cycle)) / (np.max(count_first_cycle) - np.min(count_first_cycle)) 
     
    time_x_axis=[]        
    for i in range (0,int(time/sampling_time)):
        time_x_axis.append(i)
        
    plot=matplotlib.pyplot.scatter(time_x_axis,normalized_count,color='black',
                                   s=0.5,label='Photon count') 
    
    
    df = pd.read_csv("x_y_robot_position.txt", sep=",")
    pos_x=[]
    for i in range(index):
        pos_x.append(df.iat[i, 0]-df.iat[0,0])

    normalized_pos = (pos_x - np.min(pos_x)) / (np.max(pos_x) - np.min(pos_x))
    time= np.loadtxt("./time.txt")
    time_vector=[]
            
    #(index*2) is becuase we record the time before and after 
    #each position recording to do average for the sake of precision
    lag=12.8
    for i in range (0,(index*2)):      
        if (i % 2) == 0:
            average = (((time[i]+time[i+1])/2)+lag) #13 is the lag time
            time_vector.append((average*100))
    
    plot=matplotlib.pyplot.scatter(time_vector,normalized_pos,color='red',
                                   label='Position_x',s=0.05)      
    plt.xlabel(r'Sampling time',size=18)
    plt.savefig("one cycle",dpi=500)
##############################################################################  


##############################################################################
time=60000
sampling_time=10
index=3459
cross_correlation(time,sampling_time,index)
visualisation(time,sampling_time,index)
##############################################################################










