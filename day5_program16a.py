def extract_consonants(s):
    temp_consonants=''
    for i in s:
        if i in 'QWRTYPASDFGHJKLZXCVBNMbqwrtypsdfghjklzxcvbnm':
            temp_consonants+=i
    return temp_consonants
str1=input()
a=extract_consonants(str1)
print("consonents:",a)
