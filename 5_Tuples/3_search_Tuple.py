#Search in tuple
a=('a','b','c','d','e')

print("f" in a)

#2
def search(a,val):
    for i in a:
        if i==val:          #Time O(n) Space O(1)
            return a.index(i)
    return "Not Found"

print(search(a, "b"))
    
