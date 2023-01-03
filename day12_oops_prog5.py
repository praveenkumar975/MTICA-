class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
        
    def perimeter(self):
        temp= 2*self.pi*self.radius
    def area(self):
        temp= self.pi*self.radius**2
        return temp
        
r=int(input())
ob=Circle(r)
area=ob.area()
peri=ob.perimeter()
print('Area of a circle with radius',r,'is',area)
print('Perimeter of a circle with radius',r,'is',peri)
