fo1=open(r"D:\pythonpractice46\day10\da10a.txt","r")
fo2=open(r"D:\pythonpractice46\day10\MTICA.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File Copied")
