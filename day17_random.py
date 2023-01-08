from random import *
print(random())

print(randint(1,100))
#you can use the uniform() funtion
print(uniform(1,10))

#We can shuffle a list with this code:
items=[1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)
#To pick a random number from a list:
items=[1,2,3,4,5,6,7,8,9,10]
x=sample(items,3)
print(x[0])
y=sample(items,4)
print(y)
