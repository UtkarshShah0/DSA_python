
a=[1,2,3,4,5]
a[0] = 100    #Time Complexity O(1)"""
a[1] = 1000   #"""Space Complexity O(1)"""
print(a)

a.insert(0,11)      #Time O(n) Space O(1)
print(a)

a.append(55)     #Time O(1) and Space O(1)

a.extend([50,60,70,80])  #Time O(n) and Space O(n)
