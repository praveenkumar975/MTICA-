import math
def checkArmstrongnumber(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total +=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
inpnum=int(input("Enter no:"))
if checkArmstrongnumber(inpnum):
    print("yes")
else:
    print("no")
