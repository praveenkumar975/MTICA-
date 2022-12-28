def replacenum(n):
    n=str(n)
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n
inp=int(input("replace no:"))
print(replacenum(inp))
