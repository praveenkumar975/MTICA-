class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        temp=self.real+ob.real,self.imag+ob.imag
        return temp
    def __sub__(self,ob):
        temp=self.real-ob.real,self.imag-ob.imag
        return temp
    def __mul__(self,ob):
        temp=(self.real*ob.real-self.imag*ob.imag,
              self.real*ob.imag+self.imag*ob.real)
        return temp
    def __str__(self):
        return (self.real,self.imag)


ob1=Complex(3,5)
ob2=Complex(5,7)
ob4=ob1+ob2
ob354=ob1-ob2
ob3=ob1*ob2
print(ob3)
print(ob4)
print(ob3)
