def printMonth(dn):
    mn=''
    if(dn==1):
       mn= "Janvary"
    elif(dn==2):
       mn= "Febravary"
    elif(dn==3):
        mn= "March"
    elif(dn==4):
        mn= "April"
    elif(dn==5):
        mn= "May"
    elif(dn==6):
        mn= "Jun"
    elif(dn==7):
        mn= "July"
    elif(dn==8):
        mn= "Augest"
    elif(dn==9):
        mn= "September"
    elif(dn==10):
        mn= "Octomber"
    elif(dn==11):
        mn= "November"
    elif(dn==12):
        mn= "December"
    else:
        mn= "invalid"
    return mn


for i in range(12):
    inpNum=int(input())
    print(printMonth(inpNum))
