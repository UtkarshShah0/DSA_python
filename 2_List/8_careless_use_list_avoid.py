#caressless use of list how to avoid
a=[6,75,2,3,1]
a=a.sort()
print(a)


a=[6,75,2,3,1]
a.append(10)#avoid
a=a+[20]    #use
print(a)
