import numpy as np
import pandas as pd
import csv
import os

fList = os.listdir('C:/Users/S/test/BTech/X_TrainConverted')
#fList = os.listdir('C:/Users/S/test/BTech/X_TestConverted')
print(fList)
allFiles = pd.DataFrame()

for f in fList:
    file_csv = pd.read_csv('C:/Users/S/test/BTech/X_TrainConverted/'+f)
    #file_csv = pd.read_csv('C:/Users/S/test/BTech/X_TestConverted/'+f)
    #print("Done")
    allFiles = allFiles.append(file_csv)

allFiles.to_csv("X_Train.csv", index = False)
#allFiles.to_csv("X_Test.csv", index = False)