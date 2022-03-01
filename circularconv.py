#circular convolution
import numpy as np
def circular_convolution(x,h):
    y=[]
    a=np.array(x[0])
    b=np.array(x[:0:-1])
    p=np.insert(b,0,a)
    y.append(p)
    for i in range(len(x)-1):
        p = np.roll(p,1)
        y.append(p)
    u=[]
    for t in y:
        u.append(np.dot(t,h))
    return u