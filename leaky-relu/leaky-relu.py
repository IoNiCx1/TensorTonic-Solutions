import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    x = np.asarray(x,dtype  =float)
    for i in range(len(x)):
        if x[i]<0:
            x[i] = alpha*x[i]
        else:
            x[i] = np.maximum(0,x[i])
    return x