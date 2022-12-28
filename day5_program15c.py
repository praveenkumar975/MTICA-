def removevowel(s):
    temp=''
    for i in s:
        if i not in 'AEIOUaeiou':
            temp +=i
    return temp
str1=input()
a=removevowel(str1)
print(a)
