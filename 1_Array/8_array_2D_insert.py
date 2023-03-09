'''Insertion of element in 2d '''

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

b=np.insert(a,1,[[11,22,33,44]], axis=1)
print(b)

c=np.insert(a,1,[[11,22,33,44]], axis=0)
print(c)

d=np.append(a, [[90,80,70,60]], axis=0)
print(d)

