#Question 3
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])

def search(num, target):
    for i in range(len(a)):
        if(a[i]==target):
            return i
print(search(a,8))
