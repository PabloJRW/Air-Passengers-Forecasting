import numpy as np
import pandas as pd

def difference(dataset):
    diff = list()
    diff2 = list()
    
    dataset = np.log(dataset)
    
    for i in range(1, len(dataset)):
        value = dataset[i] - dataset[i - 1]
        diff.append(value)
            
    for i in range(1, len(diff)):
        value = diff[i] - diff[i-1]
        diff2.append(value)
    
    return pd.Series(diff2)