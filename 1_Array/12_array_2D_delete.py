'''Deleting an element in an 2D array'''
import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

b=np.delete(a, 1, axis=0)
print(b)
