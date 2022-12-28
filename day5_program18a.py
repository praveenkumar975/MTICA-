def extract_specialcharacters(s):
    temp_specialcharacters=''
    for i in s:
        if i not in 'AEIOUaeiouQWRTYPASDFGHJKLZXCVBNMbqwrtypsdfghjklzxcvbnm0987654321':
            temp_specialcharacters+=i
    return temp_specialcharacters
str1=input()
a=extract_specialcharacters(str1)
print("specialcharaters:",a)
