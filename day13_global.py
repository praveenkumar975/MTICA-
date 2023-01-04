X=5;y=7
def changeme(mylist):
    "This function demonstrates local and global variables"
    p=89
    global x,y
    x=y+2
    mylist=[1,2,3,4] #this would assign new reference in my list
    print("Values inside the functio :",mylist)
    print("local varibales are:",locals())
    print("global variables are:",globals())
    return
#now you can call change me funtion
mylist_var=[10,20,30]
changeme(mylist_var)
print("Values outside the funtion:",mylist_var)
