#Q6 Permutation

def per(a,b):
    if(len(a)!=len(b)):
        return False
    a.sort()
    b.sort()
    return a==b

print(per(["a","b","c"],["c","b","a"]))
