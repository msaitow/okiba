from numpy import linalg as la
import numpy as np

dim    = 1000
xinit  = -30.0
xfinal =  30.0
dx     = (xfinal-xinit)/dim

hbar = 1.0
m    = 1.0

def formKinetic():
    k = np.zeros([dim,dim])
    for i in range(dim):
        for j in range(i,dim):
            fac = hbar**2 / (2*m) * (-1.0)**(i-j) / dx**2.0 
            if i==j: k[i,j] = fac * np.pi**2 / 3.0
            else:    k[i,j] = k[j,i] = fac * 2 / (i-j)**2
    return k
            
def formPotential():
    k     = 10.0
    omega = np.sqrt(k/m)
    v = np.zeros([dim,dim])
    for i in range(dim):
        x = xinit + i*dx
        v[i,i] = 0.5*k*x**2
    return v

def calcEnergies():
    k     = 10.0
    omega = np.sqrt(k/m)
    e = np.zeros([dim])
    for i in range(dim): e[i] = hbar*omega*(i+0.5)
    return e

if __name__ == '__main__':
    t = formKinetic()
    v = formPotential()
    h = t + v
    edvr, psi = la.eigh(h)
    eexact = calcEnergies()
    print("Energies (DVR)")
    print(edvr)
    print("Ladder spacing")
    eold = edvr[0]
    enew = 0.0
    de = np.zeros([dim-1])
    for i in range(dim):
        if i == 0: continue
        else:
            de[i-1] = edvr[i]-eold
            eold    = edvr[i]
    print(de)
    print("Energies (Exact)")    
    print(eexact)
    error = edvr-eexact
    idx = -1
    for i in range(error.shape[0]):
        if abs(error[i]) >= 1.0e-10:
            idx = i
            break
    print("Energies (Errors)")    
    print(error)
    print("Last index")
    print(idx)
    
    
    
    
