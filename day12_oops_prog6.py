class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'INVALID'
        self.length=length
        self.width=width
    def perimeter(self):
        return self.length*self.width
    def area(self):
        return 2*(self.length+self.width)

l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.area()
    peri=ob.perimeter()
    print('Perimeter of ractangle is',peri)
    print('Area of ractangle is',area)
except AssertionError as obj:
    print(obj)
