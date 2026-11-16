import numpy as np

def matrix_trace(A: list) -> float:
    
    A = np.asarray(A)
    n,m = A.shape
    k = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                k += A[i,j]
    return k