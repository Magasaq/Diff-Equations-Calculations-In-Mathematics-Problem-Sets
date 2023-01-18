import numpy as np
from scipy.linalg import solve
import math as math
import matplotlib.pyplot as plt
from Jak import jacobi
from Sel import sel
from SOR import sor_solver
def RealSoulution(N):# creation of real soultuion values
	h = 2*math.pi/N
	Y = np.zeros(N)
	for i in range(0,N):
		x = (h*i-h/2-math.pi)
		Y[i] = math.cos(x/2)**2
	return Y
def GenOfInitMatrix(N,lamda): # creation of initial matrix
	E = np.eye(N)
	A = np.zeros((N,N))
	b = np.zeros(N)
	h = 2*math.pi/N
	for i in range(0,N):
		for j in range(0,N):
			K = h*h*abs(i-j)
			x = (h*i-h/2-math.pi)
			b[i] = (1+2*lamda)*math.cos(x/2)**2 - lamda*(x**2+math.pi**2)/2
			A[i][j] = E[i][j] - lamda*K
	return A,b
lamda =  0.01
N = 100 # Number of matrix
xRealSol = RealSoulution(N)
A,b = GenOfInitMatrix(N,lamda)
n = 100 # noumber of iterations
# jakobi soulution start
y = np.ones(N)
xJak = jacobi(A, b, y, n)
# SelSuol
xSel = sel(A,b)
# SorSoul
residual_convergence = 1e-8
omega = 0.5
xSor = sor_solver(A, b, omega, y, residual_convergence)
#np.savetxt("Real.txt", xSol, fmt="%s")
#np.savetxt("Jakob.txt", x, fmt="%s")
print("xJak=",xJak)
print("xSel=",xSel)
print("xSor=",xSor)