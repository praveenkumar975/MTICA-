#print('{},{},{}'.format('apple','banana','carrot'))
'''apple,banana,carrot'''
#print('pravin purchased a kg of {},a dozan of {} and half kg of {}'.format('apple','banana','carrot'))
'''pravin purchased a kg of apple,a dozan of banana and half kg of carrot'''


print('{0},{1},{2}'.format('apple','banana','carrot','pen'))


print('{0},{1},{2}'.format('apple','banana','carrot'))


print('{2}, {1},{1}, {0}'.format('apple','banana','carrot'))



x,*y,z='computer'
print(x)
print(y)
print(z)

*x,y='abcd'
print(x)
print(y)



print('coordinates:{latitude},{longitude}'.format(latitude='37.24N',longitude='-115.81W'))


print('welcome:{name},your college is:{college}'.format(name='pravin',college='MTICA'))
