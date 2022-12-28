string=input()
ans=[]
for i in string:
    if i not in 'AEIOUaeiou':
        ans.append(i)
print(*ans)


print([i for i in string if i not in 'AEIOUaeiou'])
