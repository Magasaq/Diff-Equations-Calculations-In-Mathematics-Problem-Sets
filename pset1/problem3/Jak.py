import numpy as np
from scipy.linalg import solve
import math as math
import matplotlib.pyplot as plt
def jacobi(A, b, x, n):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(n):
        x = (b - np.dot(R,x))/ D
    return x

