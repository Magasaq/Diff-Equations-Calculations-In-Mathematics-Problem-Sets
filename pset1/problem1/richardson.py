import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg as spla
import scipy
#from scipy.sparse import csc_matrix
#A = np.array([[1, 2, 3], [1, 3, 5], [1, 2, 4]])
def Rich(A,b,n):
	rhs = b
	ev1, vec = spla.eigsh(A, k=2, which='LA')
	ev2, vec = spla.eigsh(A, k=2, which='SA')
	lam_max = ev1[0]
	lam_min = ev2[0]
	tau_opt = 2.0/(lam_max + lam_min)
	niters = 100
	x = np.zeros(n)
	res_richardson = []
	for i in range(niters):
	    rr = A.dot(x) - rhs
	    x = x - tau_opt * rr
	    res_richardson.append(np.linalg.norm(rr))
	#Convergence of an ordinary Richardson (with optimal parameter)
	#print(res_richardson)
	plt.plot(res_richardson)
	plt.yscale('log')
	plt.xlabel("Number of iterations", fontsize=20)
	plt.ylabel("Residual norm", fontsize=20)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	print("Maximum eigenvalue = {}, minimum eigenvalue = {}".format(lam_max, lam_min))
	print("Condition number = {}".format(lam_max.real / lam_min.real))
	return x