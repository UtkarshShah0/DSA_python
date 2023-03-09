#Question 4
import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9])

def product(array):
    b=0
    for i in range(len(array)): 
        for j in range(i+1, len(array)):
            if(array[i]*array[j]>b):
                b = array[i]*array[j]
    return b

print(product(a))
            
        
