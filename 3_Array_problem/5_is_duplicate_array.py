#Q5 Find if array contain duplicate elements

def dup(array):
    a=[]
    for i in array:
        if i in a:
            return False
        else:
            a.append(i)
    return True


print(dup([1,2,3,4]))
