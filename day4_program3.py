import math
def checkprimenumber(num):
    if num<1:
        return 0
    if num==1:
        return num
    count=int(math.sqrt(num)+1)
    for i in range(2,count):
        if num%i==0:
            return 0
    return num
start=int(input("enter first num:"))
stop=int(input("enter last num:"))
list=[]
for i in range(start,stop+1):
    if checkprimenumber(i):
        list.append(i)
print(*list)
print(len(list))
