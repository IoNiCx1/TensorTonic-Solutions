import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    if np.isclose(np.linalg.det(A), 0):
        return None
    return np.linalg.inv(A)