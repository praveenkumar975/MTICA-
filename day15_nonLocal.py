''' make funtion inside a funtion'''

def myfun1():
    x="John"
    def myfun2():
        nonlocal x
        x="hello"
    myfun2()
    return x
print(myfun1())
