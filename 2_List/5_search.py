
a=[10,20,30,40,50,60]
#In operator
if(40 in a):
    print(a.index(40))

#Linear Search
for i in a:
    if i==40:
        print(a.index(40))

#Time O(n)
#Space O(1)
