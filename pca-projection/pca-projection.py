import numpy as np

def pca_projection(X: list, k: int) -> list:
    x = np.array(X,dtype  = float)
    m,n = x.shape
    mu = np.mean(x,axis = 0)
    for i in range(m):
      for j in range(n):
        x[i][j] -= mu[j]
    C = (np.transpose(x)@x)/(m-1)
    eigen = np.linalg.eigh(C)
    s, V = eigen
    sorted_s = np.argsort(s)[::-1]
    sorted_v =V[:,sorted_s]
    W  = sorted_v[:,:k]
    return (x@W).tolist()
    