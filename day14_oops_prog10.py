#indirect inheritance or multilevel inheritance.
class A:
    def first_method(self):
        print("Method of class A......")
class B(A):
    def second_method(self):
        print("Method of class B......")
class c(B):
    def third_method(self):
        print("Method of class C......")

if __name__=='__main__':
    ob=c()
    ob.first_method()
    ob.second_method()
    ob.third_method()
#circular inheritance is not possible class A.
  
