import pyedflib as prd
import numpy as np

# read an edf file
signals, signal_headers, header = prd.highlevel.read_edf('Subject00_1.edf')
#print(signal_headers[0]['sample_rate'])
#print(signals.size)
print(header)
sh = np.array(signal_headers)
print(sh.size)
sig = np.array(signal_headers)
print(sig.size)
#print(signals)