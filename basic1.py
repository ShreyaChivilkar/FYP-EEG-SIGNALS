import pyedflib as prd
import numpy as np
import pandas as pd
import os

fList = os.listdir('C:/Users/S/test/BTech/eeg-during-mental-arithmetic-tasks-1.0.0')
x = []

# read an edf file 
                  
for item in fList:

    signals, signal_headers, header = prd.highlevel.read_edf('C:/Users/S/test/BTech/eeg-during-mental-arithmetic-tasks-1.0.0/'+item)
    x.append(signals)
    
df = pd.DataFrame(x)
df.to_csv("File1.csv")



