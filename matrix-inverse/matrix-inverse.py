import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    A = np.asarray(A,dtype  = float)
    n = A.shape[0]
    aug = np.concatenate((A,np.eye(n)),axis = 1)
    for i in range(n):
        p = i + np.argmax(np.abs((aug[i:,i])))
        if abs(aug[p,i]) < 1e-12:
            return None
        aug[[i,p]] = aug[[p,i]]
        aug[i] /= aug[i,i]
        for j in range(n):
            if j != i:
                aug[j]-= aug[j,i]*aug[i]
    return aug[:,n:]