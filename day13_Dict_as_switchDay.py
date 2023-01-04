def printSun():
    print('Sunday')
def printMon():
    print('Monday')
def printTues():
    print('Tuesday')
def printwedns():
    print('wednsdayS')
def printThurs():
    print('Thursday')
def printFri():
    print('Friday')
def printSatur():
    print('Saturday')
def choice():
    print("Enter day number between 1-7")
dayDict={1:printSun,2:printMon,3:printTues,4:printwedns,5:printThurs,6:printFri,7:printSatur}
choice()
day=int(input())
if (day>=1) and (day<=7):
    dayDict[day]()
else:
    print("INVALID")



