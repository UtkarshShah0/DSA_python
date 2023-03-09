'''Traversing an element in an 2D array'''
import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def traver(array):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print("")

traver(a)

'''Time complexity O(mn) and Space Complexity O(1) '''

