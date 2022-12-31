Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic1={'Name':'pravin','Age':23,'Course':'MCA'}
print(dic1)
{'Name': 'pravin', 'Age': 23, 'Course': 'MCA'}
print(dic1['Name'])
pravin
print(dic1['Age'])
23
print(dic1['Course'])
MCA
dic1['Age']=22
print(dic1)
{'Name': 'pravin', 'Age': 22, 'Course': 'MCA'}
dic1['College']=MTICA
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dic1['College']=MTICA
NameError: name 'MTICA' is not defined
dic1['College']='MTICA'
print(dic1)
{'Name': 'pravin', 'Age': 22, 'Course': 'MCA', 'College': 'MTICA'}
del dic1['College']
print(dic1)
{'Name': 'pravin', 'Age': 22, 'Course': 'MCA'}
del dic1['Course']
print(dic1)
{'Name': 'pravin', 'Age': 22}
dic1.clear()
print(dic1)
{}
dic1={'Name':'pravin','Age':23,'Course':'MCA'}
print(dic1)
{'Name': 'pravin', 'Age': 23, 'Course': 'MCA'}
del dic1
print(dic1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(dic1)
NameError: name 'dic1' is not defined. Did you mean: 'dict'?
dic1={'Name':'pravin','Age':23,'Course':'MCA'}
print(dic1)
{'Name': 'pravin', 'Age': 23, 'Course': 'MCA'}
dic1.keys()
dict_keys(['Name', 'Age', 'Course'])
dic1.values()
dict_values(['pravin', 23, 'MCA'])
dic1.items()
dict_items([('Name', 'pravin'), ('Age', 23), ('Course', 'MCA')])
for i in dic1:print(i)

Name
Age
Course
for i in dic1.keys():print(i)

Name
Age
Course
for i,j in dic1.items():print(i,j)

Name pravin
Age 23
Course MCA
for i in dic1.values():print(i,j)

pravin MCA
23 MCA
MCA MCA
