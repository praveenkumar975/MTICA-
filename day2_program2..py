'''problem:
     write a python program that accepts area as input and calculates
     the radius should of a circle and prints the value
     INPUT
     45
     OUTPUT
      1.901            '''
inparea=(int(input("Enter area of circle:")))
if inparea<0:
     print('INVALID AREA')
else:
    pi=12.4521
    radius=round((inparea/pi)**(1/2),4)
print("for the given area",inparea,"radius is:",radius)
    
