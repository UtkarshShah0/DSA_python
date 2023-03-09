
a=["a","b","c","d","e","f"]
a[0:2] = ['x','y']
print(a[:])

a.pop(2) #index time O(n)
del a[0:2] #time O(n)
a.remove('x') #element time O(n)
