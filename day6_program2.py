lsteven=[]
lstodd=[]
while(True):
    inpnum=int(input("enter a vale(-1 to end):"))
    if inpnum==-1:
        break
    elif inpnum%2==0:
        lsteven.append(inpnum)
    elif inpnum%2==1:
        lstodd.append(inpnum)
print("even:",*lsteven)
print("min:",min(lsteven))
print("max:",max(lsteven))
print("avg:",round(sum(lsteven)/len(lsteven),1))

print("odd:",*lstodd)
print("min:",min(lstodd))
print("max:",max(lstodd))
print("avg:",round(sum(lstodd)/len(lstodd),1))
