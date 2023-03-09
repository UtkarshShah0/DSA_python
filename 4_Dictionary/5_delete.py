#4 delete dict

a={'name': 'Edy', 'age': 27, 'address': 'London', 'education':'master'}

#pop()
print(a.pop('name'))
print(a)

#pop.item() no parameter
print(a.popitem())
print(a)

#.clear() deletes all items
a.clear()
print(a)

#del
#del a["age"]

del a                                   #Time complexity : O(1)
print(a) #Error doesnot exist a         #Time amortized : O(n)
                                        #Space Complexity: O(1)
