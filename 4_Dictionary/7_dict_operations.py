#Dict Methods

a={'name': 'Edy', 'age': 27, 'address': 'London', 'education':'master'}

#in operator
print('name' in a)
print('Edy' in a)

print("keys")
for i in a:     #for keys
    print(i)

print("values")
for i in a.values():  #For values
    print(i)

#All func
b={1: True, 2: True}
print(all(b))
c={}
print(all(c))

#Any Func
b={1:True, 2:False}
print(any(b))
print(any(c))


#Len Func
print(len(a))

#Sorted Func
print(sorted(a, reverse= True))
print(sorted(a, key=len))
