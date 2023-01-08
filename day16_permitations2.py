from itertools import permutations
print("All the permutations of the given list is:")
print(list(permutations([1,'mtca'],2)))
print()
print(list(permutations([1,'mtica','crt'])))
print()
print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()
print("All the permutations of the given container\
      is")
print(permutations(range(3),2))
