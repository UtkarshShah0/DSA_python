'''No matter what if index greater then the length of the array then
value will be added to the last element of array'''
from array import *
a = array('i',[1,2,3,4,5])
a.insert(10,7)

print(a)
a.insert(0,6)
print(a)

'''Time complexity at the beginning of the array is O(n) and at the end is O(1)
'''
