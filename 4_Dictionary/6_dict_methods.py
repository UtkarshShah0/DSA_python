#6 Dictionary Methods

a={'name': 'Edy', 'age': 27, 'address': 'London', 'education':'master'}

#a.clear()      #1
print(a)

b=a.copy()      #2
print(b)

newdict = {}.fromkeys([1,2,3],0)        #3
print(newdict)

print(a.get("city","Not found"))        #4
print(a.get("age","Not found"))

print(a.keys())                 #5

print(a.popitem())          #6
print(a)

print(a.setdefault('name1','added')) #7
print(a)

print(a.values())           #8

c={"a":1,"b":2,"c":3}
a.update(c)                 #9

print(a)
