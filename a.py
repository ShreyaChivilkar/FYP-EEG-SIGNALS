import pyedflib as prd
import numpy as np
import pandas as pd
import csv
import os

fList = os.listdir('C:/Users/S/test/BTech/X_Test')
#fList = os.listdir('C:/Users/S/test/BTech/X_Train')
y = []

# read an edf file 
                  
for item in fList:

    
    file = item.split('.')[0]
    if file.endswith('_1'):
        y_train = 0
    elif file.endswith('_2'):
        y_train = 1

    #print(y_train)

    p = (np.ones(91000))
    #print(p.size)
    
    y1 = p * y_train
    #print(y1)
    y = np.concatenate((y,y1))
    #print(y)


df = pd.DataFrame(y)
print(df)
df.to_csv("Y_Test"+".csv", index = False)
#df.to_csv("Y_Train"+".csv", index = False)




    


