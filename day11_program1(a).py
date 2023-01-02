def findFrequency(s):
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
            frequencyDict[i]+= 1
        else:
            frequencyDict[i]=1
    return frequencyDict
def sortedkey(d):
    for i in sorted(d.items(),key=lambda x:x[1],reverse=True):
        print(i[0],i[1])
        
n=int(input())
for i in range(n):
    inpstr=input()
    sortedkey(findFrequency(inpstr))
