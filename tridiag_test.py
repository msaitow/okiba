from scipy import linalg
import numpy as np

a = [1,2,3]
b = [-0.5,-0.8]
w, U = linalg.eigh_tridiagonal(a,b)

print(U @ np.diag(w) @ U.T)

