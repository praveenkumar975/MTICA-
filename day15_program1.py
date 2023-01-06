p=input().split()
k=input().split()
ans=[]
for i,j in zip(p,k):
    ans.append(int(i)+int(j))
    print(*ans)
