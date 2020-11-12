import pyedflib as prd
import numpy as np
import pandas as pd
import csv
import os

fList = os.listdir('C:/Users/S/test/BTech/X_Train')
x = []

# read an edf file 
                  
for item in fList:

    signals, signal_headers, header = prd.highlevel.read_edf('C:/Users/S/test/BTech/X_Train/'+item)
    x.append(signals)
    

for i in range(0,58):
    df = pd.DataFrame(np.transpose(x[i]))
    df.to_csv("File"+str(i)+".csv", index = False)                     # Create csv files

