from array import *

a = array('i',[1,2,3,4,5])

def access(array, index):
    if(index >= len(array)):
        print("Invalid Index")

    else:
        print(array[index])

access(a, 4)
