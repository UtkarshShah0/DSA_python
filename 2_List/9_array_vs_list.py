#array vs  list
import numpy as np
a=np.array([1,2,3])
print(a/2)

#b=[1,2,3]
#print(b/2)
#error

a=np.array([1,2,3,'a']) #convert everything to string
b=[1,2,3,'a']
print(a)
print(b)
