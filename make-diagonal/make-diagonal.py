import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    v = np.array(v)
    t = np.zeros((v.size,v.size),dtype = v.dtype)
    k = v.size
    for i in range(k):
        for j in range(k):
            if i == j:
                t[i,j] = v[i]
    return t