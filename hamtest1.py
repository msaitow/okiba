# (c) 2022 Masaaki Saitow (msaitow514@gmail.com)
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
import numpy as np
import time as tm
import random as rd
from functools import reduce

dim1 : int = 100
dim2 : int = 300
dim  : int = dim1 + dim2

if __name__ == '__main__':
    tinit = tm.perf_counter()
    a11 : np.ndarray = np.zeros([dim1,dim1])
    for i in range(dim1):
        for j in range(dim1):
            a11[i,j] = rd.random()
    a11 = (a11 + a11.transpose())/2.0
    eval_a, evec_a = np.linalg.eigh(a11)
    print('Eval(a)')
    print(eval_a)
    afull : np.ndarray = np.zeros([dim,dim])
    for i in range(dim1):
        for j in range(dim1):
            afull[i,j] = a11[i,j]
        for j in range(dim1,dim):
            val : float = rd.random()
            afull[i,j] = afull[j,i] = val            
    eval, evec = np.linalg.eigh(afull)
    print('Eval(full)')
    print(eval)    
    tfinal = tm.perf_counter()
    print("Elapsed time: {0:.2f} sec.".format(tfinal-tinit))
    
    
    
