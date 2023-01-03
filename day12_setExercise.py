sample_set={"Yelow","Orange","Black"}
sample_list=["Blue","Green","Red"]
sample_set.update(sample_list)
print(sample_set)






#method-1
for i in sample_list:
    sample_set.add(i)
print(sample_set)               
