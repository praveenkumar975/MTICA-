'''check a even or odd numbers'''
inpnum=int(input())
if inpnum<0:
    print("INVALID")
elif inpnum%2==0:
    print("even")
else:
    print("odd")
