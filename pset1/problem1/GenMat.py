import numpy as np
from scipy.sparse import spdiags
import math
import scipy as sp
import math
def GenMat(N,alpha):
	k = math.sqrt(alpha/3.14)
	As = np.ones((2*N-1,2*N-1))
	Xr = np.ones(N+1)
	Place = np.arange(-N+1,N,1)
	arr1 = np.arange(0,N,1)
	arr2 = np.arange(N-1,0,-1)
	Pow = np.concatenate((arr2, arr1))
	data = np.exp(-alpha*Pow)
	Mat = As*data
	Mat = Mat.T
	A = spdiags(Mat, Place, N, N,'csr')
	return A
