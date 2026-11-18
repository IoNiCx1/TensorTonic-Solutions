import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    X = np.asarray(X)
    cen = X - np.mean(X,axis = 0)
    return cen.T@cen/(X.shape[0]-1)
    
                
    