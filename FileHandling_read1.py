fo=open(r"D:\pythonpractice46\day9\abc.txt","r")
inpStr=input('Enter text:')
fo.write(inpStr)
inpstr=input('Enter text;')
fo.write(inpStr)
temp=fo.read()
fo.close()
print(temp)
