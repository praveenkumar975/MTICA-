#dog class inhertis from wolf class with the same attribute or methods,
#it overrides them
class Wolf:
    price=500
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr....")
class Dog(Wolf):
    def bark(self):
        print("Woof")
        
pet1=Dog("tomy","brown")
pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()
#redifining a method of base class in derived class is overriding
