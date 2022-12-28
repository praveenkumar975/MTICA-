string='''
practice problems for list com pre hension in python'''

wordslist=string.split(' ')
ans=[i for i in wordslist if len(i.strip('\n'))==8]
print(*ans)
