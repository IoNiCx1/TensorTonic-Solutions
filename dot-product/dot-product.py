import numpy as np

def dot_product(x: list, y: list) -> float:
    su = float(0) 
    for i in range(len(x)):
        su  += x[i]*y[i]
    return su