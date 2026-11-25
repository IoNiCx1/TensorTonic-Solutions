import numpy as np

def tanh(x: list) -> np.ndarray:
    x = np.array(x,dtype  =float)
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))