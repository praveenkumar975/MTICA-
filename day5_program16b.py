def count_consonents(s):
    n_consonents=0
    for i in s:
        if i in 'QWRTYPASDFGHJKLZXCVBNMbqwrtypsdfghjklzxcvbnm':
            n_consonents+=1
    return n_consonents
str1=input()
a=count_consonents(str1)
print("No of consonents in:'",str1,"'is",a)
