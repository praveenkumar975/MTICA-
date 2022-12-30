def printMonth(dn):
    if(dn==1):
        return "Janvary"
    elif(dn==2):
        return "Febravary"
    elif(dn==3):
        return "March"
    elif(dn==4):
        return "April"
    elif(dn==5):
        return "May"
    elif(dn==6):
        return "Jun"
    elif(dn==7):
        return "July"
    elif(dn==8):
        return "Augest"
    elif(dn==9):
        return "September"
    elif(dn==10):
        return "Octomber"
    elif(dn==11):
        return "November"
    elif(dn==12):
        return "December"
    else:
        return "invalid"


for i in range(12):
    inpNum=int(input())
    print(printMonth(inpNum))
