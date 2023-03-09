'''Accessing an element in an 2D array'''
import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def acces(array, rowind, colind):
    if rowind >= len(a) and colind >= len(a[0]):
        print("Invalid Index")
    else:
        print(a[rowind][colind])

acces(a,3,3)

