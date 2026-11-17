import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    sum = 0 
    for i in range(len(x)):
        sum += abs(x[i]-y[i])
    return float(sum)