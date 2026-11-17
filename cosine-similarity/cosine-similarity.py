import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    dot = np.dot(np.array(a),np.array(b))
    norma = np.linalg.norm(np.array(a))
    normb = np.linalg.norm(np.array(b))
    if norma == 0 or normb == 0:
        return float(0)
    return float(dot/(norma*normb))