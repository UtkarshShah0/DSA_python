#python project

a=[]
b=int(input("How many day's temperaure? "))

for i in range(b):
    c=int(input("Day %d's high temp: " %(i+1)))
    a=a+[c]
d=sum(a)/len(a)
print("Average = ",d)

count=0
for i in a:
    if(i>d):
        count +=1
print("%d day(s) above average" %count)
    
 
