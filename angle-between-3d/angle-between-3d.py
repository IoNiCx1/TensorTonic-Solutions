import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    v,w = np.asarray(v),np.asarray(w)
    a_norm = np.sqrt(np.sum(v**2))
    b_norm = np.sqrt(np.sum(w**2))
    return np.arccos((v@w)/(a_norm*b_norm))