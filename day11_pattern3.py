def printPattern(ch,n):
    assert(n>0),'INVALID'
    for i in range(n+1):
        print(ch*i)

ch=input()
n=int(input())
try:
    printPattern(ch,n)
except AssertionError as a:
    print(a)






#method-2
##def printPattern(n):
##    num=1
##    for i in range(1,n+1):
##        print(i*'*')
##
##inp=int(input())
##printPattern(inp)

