fo=open(r"D:\pythonpractice46\day10\da10a.txt","a")
for i in range(5):
        inpstr=input("Enter string:")
        fo.write(inpstr+'\n')
fo.close()
print("write to file")
