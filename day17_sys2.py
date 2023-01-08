import sys
print("Coming through stdout")

#stuout is saved

save_stdout=sys.stdout
fh=open(r"d:\pythonpractice46\day17\axd.txt","w")
sys.stdout=fh
print("This line goes to test.txt")
print(input())
#return to normal:
sys.stdout=save_stdout
fh.close()
