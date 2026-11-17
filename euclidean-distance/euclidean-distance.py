import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    su = 0 
    for i in range(len(x)):
        su += (x[i]-y[i])**2
    return np.sqrt(su)