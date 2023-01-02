sample_dict = {
    "name": "Pravin",
    "age": 22,
    "salary": 80000,
    "city": "India"
}
keys=["name","salary"]

newDict={}
for i in  keys:
    newDict[i]=sample_dict[i]
print(newDict)

#method-1
newDict={i:sample_dict[i] for i in keys}
print(newDict)


#method-2
res=dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)


#method-3
for k in keys:
    sample_dict.pop(k)
print(sample_dict)
