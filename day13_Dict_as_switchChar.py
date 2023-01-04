def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMul(a,b):
    return a*b
def printDivi(a,b):
    return a/b
def choice():
    print("+:Adition")
    print("-:Substraction")
    print("*:Multiplication")
    print("/:Division")
    print("q:Quit")
    return
colorselect={"+":printAdd,"-":printSub,"*":printMul,"/":printDivi}
while True:
    choice()
    selection=input("select an arithmatic operation:")
    if selection=='q' or selection=='Q': break
    if ((selection=='+') or (selection=='-') or
    (selection=='*') or (selection=='/')):
        n1=int(input("Enter first no:"))
        n2=int(input("Enter second no:"))
        z=colorselect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
