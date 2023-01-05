#inheritance is a way to share funtionality between classes.
class Animal:  #superclass
    def __init__(self,name,color):
        self.name=name
        self.color=color
#cat and dog are subclass
class Cat(Animal): 

    def mew(self):
        print("cat meows")
class Dog(Animal):
    def bark(self):
        print("Wolf")
if __name__=="__main__":
    print(__name__)
    pet1=Dog("tomy","brown")
    pet2=Cat("lucy","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
