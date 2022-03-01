import numpy as np
import matplotlib.pyplot as plt
n=np.arange(-3,9)
x=np.zeros_like(n)
#x[(n>=0)&(n<=4)]=n[(n>=0)&(n<=4)]#ramp
#x[n==0]=1#unitpulse
#x[(n>=0)&(n<=4)]=n[(n>=0)&(n<=4)]
#x[(n>=5)&(n<=8)]=8-n[(n>=5)&(n<=8)]
#x[(n>=0)&(n<=2)]=1
#x[(n>=3)&(n<=5)]=-1
plt.xticks(n)
plt.stem(n,x)

plt.show()