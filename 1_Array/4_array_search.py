from array import *

a=array("i",[1,2,3,4,5])
def search(array, value):
    for i in array:
        if i==value:
            return array.index(value)
    return ("The value does not exist")

b=search(a,4)
print(b)
