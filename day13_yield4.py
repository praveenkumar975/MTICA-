def squares(x=0):
    while x<100:
        x=x+1
        yield x*x

yieldedlist=list(squares())
print(yieldedlist)


#yieldedlist=[i for i in squares()]
#print(yieldedlist)
