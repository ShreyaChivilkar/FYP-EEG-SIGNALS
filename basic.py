import pyedflib as prd
import numpy as np

# read an edf file
signals, signal_headers, header = prd.highlevel.read_edf('Subject00_1.edf')

print("Information about one subject:" , header)
sh = np.array(signal_headers)
sig = np.array(signal_headers)
print("No of electrodes: ", sig.size)                              
#print("DATA", signals)    
print("Information about one electrode: ", sig[0])                          
print("Size of data in each electrode: ", signals[0].size)
print("Data in first electrode: ", signals[0])                       
