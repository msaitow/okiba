import numpy as np
import numpy.linalg as la
import copy as cp
from scipy import linalg as sl

#Generates the representation in Krylov subspace of a Hermitian NxN matrix using the Lanczos algorithm and an initial vector guess vg.
def Lanczos(H,vg):
    #Lv=np.zeros((len(vg),len(vg)), dtype=complex) #Creates matrix for Lanczos vectors
    #Hk=np.zeros((len(vg),len(vg)), dtype=complex) #Creates matrix for the Hamiltonian in Krylov subspace
    Lv=np.zeros((len(vg),len(vg))) #Creates matrix for Lanczos vectors
    Hk=np.zeros((len(vg),len(vg))) #Creates matrix for the Hamiltonian in Krylov subspace
    Lv[0]=vg/la.norm(vg) #Creates the first Lanczos vector as the normalized guess vector vg
     
    #Performs the first iteration step of the Lanczos algorithm
    w=np.dot(H,Lv[0]) 
    a=np.dot(np.conj(w),Lv[0])
    w=w-a*Lv[0]
    Hk[0,0]=a
     
    #Performs the iterative steps of the Lanczos algorithm
    for j in range(1,len(vg)):
        b=(np.dot(np.conj(w),np.transpose(w)))**0.5
        Lv[j]=w/b
         
        w=np.dot(H,Lv[j])
        a=np.dot(np.conj(w),Lv[j])
        w=w-a*Lv[j]-b*Lv[j-1]
        
        #Creates tridiagonal matrix Hk using a and b values
        Hk[j,j]=a
        Hk[j-1,j]=b
        Hk[j,j-1]=np.conj(b)
        
    return (Hk,Lv)

if __name__ == '__main__':
    #H = np.random.rand(8,8) + np.random.rand(8,8)*1j #Generates random complex-valued 8x8 matrix
    H = np.random.rand(8,8) #Generates random complex-valued 8x8 matrix
    H = H + H.conj().T #Ensures 8x8 matrix is symmetric (hermitian)
    Hc = cp.copy(H)
    a,b = np.linalg.eigh(H) #Directly computes eigenvalues of H
    #vg = np.random.rand(8) + np.random.rand(8)*1j #Generates random guess vector
    vg = np.random.rand(8) #Generates random guess vector
    Hk,Lv = Lanczos(Hc,vg) #Applies the Lanczos algorithm to H using the guess vector vg
    A,B= np.linalg.eigh(Hk)

    # Use a specific function to diagonalize tri-diagonal matrices
    # Tridiagonal elements of Hk
    x = np.zeros(len(vg))
    y = np.zeros(len(vg)-1)
    #for i in range(0,len(vg)): print(i) 
    for i in range(0,len(vg)): x[i  ] = Hk[i,i]
    for i in range(1,len(vg)): y[i-1] = Hk[i,i-1]
    w, U = sl.eigh_tridiagonal(x,y)

    print(np.get_printoptions())   

    np.set_printoptions(threshold=np.inf)   
    np.set_printoptions(edgeitems=10)   
    np.set_printoptions(linewidth=750)   
   
    print('type(Hk): ', type(Hk))
    print('Hk')
    print(Hk)

    print('a')
    print(a)
    print('A')
    print(A)
    print('w')
    print(w)

    print('b[:,0]')
    print(b[:,0])
    print('np.dot(B[:,0],Lv)')
    print(np.dot(B[:,0],Lv))

