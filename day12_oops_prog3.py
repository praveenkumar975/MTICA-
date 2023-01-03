class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.rollno=rollno
        self.name=name
    def displayStudent(self):
        print("Name: "+self.name+'\nRollno: '\
              +str(self.rollno))
        print("College: "+self.college+'\nCourse: '\
              +self.course)

for i in range(3):
    s1=input()
    s2=int(input())
    ob=Student(s1,s2)
    ob.displayStudent()






#another method
lst=[]
for i in range(3):
    s1=input()
    s2=int(input())
    temp='ob'+str(i)
    temp=Student(s1,s2)
    lst.append(temp)
for i in lst:
    i.displayStudent()
