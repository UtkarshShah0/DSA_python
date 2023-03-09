#5 tuple vs list
a=[1,2,3,4]
a[0]=10
del a[0]
print(a)

b=(1,2,3,4)
#b[0] = 10
#del b[0]

b=(4,4,4,4)
del b

#func for both len,max,min,sum,sorted,all,any,count,index

#cant be used append,insert,remove,pop,clear,sort,reverse

list1 = [(1,2),(3,4),(5,6)]
print(list1)

tuple1 = ([1,2],[3,4],[5,6])
print(tuple1)
