string= '''practice problems for list com pre hension in python'''
ans=[]
wordslist=string.split(' ')
for i in wordslist:
     if len(i)==3:
         ans.append(i)
print(*ans)
