import math

def elu(x: list, alpha: float = 1.0) -> list:
    # x = np.array(x,dtype  = float)
    return [k if k>0 else alpha*(math.exp(k)-1) for k in x]