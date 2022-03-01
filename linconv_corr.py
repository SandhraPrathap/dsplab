#linear convolution
import numpy as np
import matplotlib.pyplot as plt
'''def lin_convolution(x,h):
    M= len(x)
    N = len(h)
       
    if M!=N:
        if M>N:
            h= np.append(h,np.zeros(M-N))   
        else :
            x = np.append(x,np.zeros(N-M))
    K= max(N,M)
    y= np.zeros(N+M-1)
        
    for i in range(len(y)):
      if i<M:
        for j in range(i+1):
              y[i]+=x[j]*h[i-j]
      elif i>=M:
        for j in range(K-1,i-K,-1):
              y[i]+=x[j]*h[i-j]
        
    return y[:N+M-1]

x=np.array([1,2,3,4])
h = np.array([1,5])
y=lin_convolution(x,h)
plt.stem(y)
plt.show()'''

#correlation
def correlation(x,h):
    M= len(x)
    N = len(h)
       
    if M!=N:
        if M>N:
            h= np.append(h,np.zeros(M-N))   
        else :
            x = np.append(x,np.zeros(N-M))
    K= max(N,M)
    y= np.zeros(len(x)+len(h)-1)
    h= h[::-1]
    
        
    for i in range(len(y)):
      if i<M:
        for j in range(i+1):
              y[i]+=x[j]*h[i-j]
      elif i>=M:
        for j in range(K-1,i-K,-1):
              y[i]+=x[j]*h[i-j]
              
    if len(h)>N or len(x)>M:
      return y[(abs(N-M))::]
    else:
      return y

x=np.array([1,2,3,4])
h = np.array([1,5,7,4])
y=correlation(x,h)
plt.stem(y)
plt.show()
