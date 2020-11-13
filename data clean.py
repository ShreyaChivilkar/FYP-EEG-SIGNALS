import pyedflib as prd
import numpy as np
import pandas as pd
import os
import csv

#fList = os.listdir(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_train')
fList = os.listdir(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_test')
x = []
y = []
allFiles = pd.DataFrame()
                  
for item in fList:
    #edf to csv conversion
    #signals, signal_headers, header = prd.highlevel.read_edf(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_train'+'\\'+item)
    signals, signal_headers, header = prd.highlevel.read_edf(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_test'+'\\'+item)
    x.append(signals)
    df = pd.DataFrame(np.transpose(signals))
    fname = item.split('.')[0]
    #df.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_train_op'+'\\'+fname+'.csv', index = False) 
    df.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\X_test_op'+'\\'+fname+'.csv', index = False) 
    #To create single train file
    allFiles = allFiles.append(df)
    #Generate ylabel
    y_size = len(df.index)
    if fname.endswith('_1'):
        y_train = 0      
    elif fname.endswith('_2'):
        y_train = 1
    p = (np.ones(y_size))
    y1 = p * y_train
    y = np.concatenate((y,y1))

df = pd.DataFrame(y)
#print(df)
#df.to_csv("Y_Test"+".csv", index = False)
#df.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\final data'+'\\'+"Y_Train.csv", index = False)
#allFiles.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\final data'+'\\'+'X_Train.csv', index = False)    
df.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\final data'+'\\'+"Y_Test.csv", index = False)
allFiles.to_csv(r'D:\Local Disk E\BCI\FYP\eeg-during-mental-arithmetic-tasks-1.0.0 (1)\final data'+'\\'+'X_Test.csv', index = False)    

print(len(df.index))
print(len(allFiles.index))