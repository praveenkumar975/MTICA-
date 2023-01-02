employees=['Pravin','Ram','Vishnu']
defaults={"designation":'Developer',"salary":80000}

data=dict.fromkeys(employees,defaults)
print(data)


#individual data
print(data["Ram"])
