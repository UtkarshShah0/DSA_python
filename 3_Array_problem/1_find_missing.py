#Find the missing number

def missing(list, n):
    return (n*(n+1))/2 - sum(list)

print(missing([1,2],3))
