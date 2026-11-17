import numpy as np

def dot_product(x: list, y: list) -> float:
    
    return float(np.array(x)@np.array(y))