import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    matrix = np.asarray(matrix,dtype = float)
    if norm_type == "l1":
        norms = np.sum(np.abs(matrix),axis = axis,keepdims = True)
    elif norm_type == "l2":
        norms = np.sqrt(np.sum(np.abs(matrix**2),axis = axis,keepdims = True))
    else:
        norms = np.max(np.abs(matrix),axis = axis,keepdims = True)
    safe = np.where(norms== 0,1,norms)
    return matrix/safe
    
    