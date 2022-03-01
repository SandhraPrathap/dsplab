import numpy as np
import matplotlib.pyplot as plt

N=4
D=np.empty((N,N),dtype=np.cdouble)
W=np.exp(-1j*2*np.pi/N)#twiddle factor
 
for k in np.arange(N):
	for n in np.arange(N):
		D[k,n]=W**(k*n) #twiddle factor matrix
np.round(D)

x=np.array([[1,2,3,4]]).T#column vector
X=D@x #matrix product
np.round(X)

print("Input sequence x(n)DFT =",x)
print("DFT X(k)=",X)
		
