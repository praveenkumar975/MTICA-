## nonlocal
##first funtion

def f():
    x=10
    print('id(x) in f outer:',id(x))
    #nested funtion
    def g():
        nonlocal x
        x=15
        print('id(x) in g inner:',id(x))
    g()
    print(x)

f()
