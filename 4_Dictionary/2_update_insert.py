#2 Update Insert Key value in dict

#update add an element
mydict = {"name":"Edy","age":26}
mydict["age"] = 27

#update
#time complexity O(1)
#Space complexity O(1) 
print(mydict)

#adding
#time complexity O(1)
#Space complexity amortized O(1)
mydict["address"] = "London"

print(mydict)
