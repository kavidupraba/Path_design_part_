import numpy as np
from collections import UserDict

g=np.ones((3,3),dtype=int)
g[2,1]=5
print(g)
print(np.where(g==5))

def check2(m):
    m[0]=5
    print(m)

def check():
    m=[1,2,3]
    ma=m.copy()
    check2(ma)
    print(m)
z=[[1,2,3],[4,5,6]]
print("here")
print(len(z))
print(len(z[0]))
m=np.array(z)
print(m[0,0])
check()
y={"ty":1,"hu":3,"bn":4}
n=dict(sorted(y.items(),key=lambda x:x[0],reverse=True))
print(n)
g=sorted(y.items(),key=lambda x:x[0],reverse=True)
print(g)
h=0
h-=1
print(h)
T=list(range(0,10,1))
print(T)