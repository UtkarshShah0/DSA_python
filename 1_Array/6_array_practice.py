#Array Practice
from array import *

'''1.Create An array and traverse'''

my_arr = array('i',[1,2,3,4,5])
for i in my_arr:
    print(i,end=" ")

'''2.Access individual elements through indexes'''
print("   ")
print("Step 2")
print(my_arr[0])

'''3.Append any value to the array using append function'''

my_arr.append(10)
print("step 3")
print(my_arr)

'''4.Add any element to the array at a given index using insert function'''

print("Step 4")
my_arr.insert(0,99)
my_arr.insert(99,0)
print(my_arr)

'''5.Extend the array using extend method()'''

print("Step 5")
my_arr1 = array('i',[20,30,40])
my_arr.extend(my_arr1)
print(my_arr)

'''6.Add Elements From List Into Array Using fromList() method'''

print("Step 6")
templist = [21,22,21]
my_arr.fromlist(templist)
print(my_arr)

'''7.Remove any element using remove() method'''

print("Step 7")
my_arr.remove(21)
print(my_arr)

'''8.Remove last element using pop() method'''

print("Step 8")
my_arr.pop()
print(my_arr)

'''9.Fetch element using index index() method'''

print("Step 9")
print(my_arr.index(99))

'''10.Reverse array using reverse() method'''

print("Step 10")
my_arr.reverse()
print(my_arr)

'''11.Get array buffer info using buffer_info() method '''

print("Step 11")
print(my_arr.buffer_info())

'''12. Check the number occurence of an element using count() method'''

print("Step 12")
print(my_arr.count(22))

'''13.Convert array to string using tostring() method'''

print("Step 13")
strTemp = my_arr.tobytes()
print(strTemp)

ints = array('i')
ints.frombytes(strTemp)
print(ints)

'''14.Convert array to a list using tolist() method'''

print("Step 14")
#print(my_arr.tolist())

'''15.Append a string to char array using fromstring() method'''

print("Step 15")
my_arr2 = array('u',['a','b'])
print(my_arr2)


'''16.Slice elements from an array'''

print("Step 16")
print(my_arr[:3])
