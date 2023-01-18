import numpy as np
def sel(A,b):
  ITERATION_LIMIT = 1000
  x = np.zeros_like(b)
  for it_count in range(1, ITERATION_LIMIT):
      x_new = np.zeros_like(x)
      for i in range(A.shape[0]):
          s1 = np.dot(A[i, :i], x_new[:i])
          s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
          x_new[i] = (b[i] - s1 - s2) / A[i, i]
      if np.allclose(x, x_new, rtol=1e-8):
          break
      x = x_new
#  print("Solution: {0}".format(x))
#  error = np.dot(A, x) - b
#  print("error:",error)
  return x