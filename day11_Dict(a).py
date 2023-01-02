'''OUTPUT:
{'Pravin': 22, 'Ram': 23, 'Vishnu': 21}'''

keys=['Pravin','Ram','Vishnu']
values=[22,23,21]
d=dict()
for i,j in zip(keys,values):
    d[i]=j

print(d)
