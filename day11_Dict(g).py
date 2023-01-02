sample_dict = {
  "name": "Ram",
  "age":23,
  "salary": 80000,
  "city": "India"
}

#keys to remove
keys=["name","salary"]


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]

print(d)
