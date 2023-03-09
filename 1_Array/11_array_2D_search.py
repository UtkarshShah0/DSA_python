'''Searching an element in an 2D array'''
import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def search(array , element):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == element:
                return i,j
    return "Element Not found"
        

print(search(a, 100))

'''Time complexity O(mn) and Space Complexity O(1) '''

