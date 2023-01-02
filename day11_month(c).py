months={1:'Janvary',2:'Febravary',3:'March',4:'April',5:'May',6:'Jun',7:'July',8:'Aguest',9:'September',10:'Octomber',11:'November',12:'December'}

n=int(input())
for count in range(n):
     mn=int(input())
     if mn>=1 and mn<=12:
         print(months[mn])
     else:
         print('INVALID')





#METHOD-1
         
##def Month(dn):
##    mn=''
##    if(dn==1):
##       mn= "Janvary"
##    elif(dn==2):
##       mn= "Febravary"
##    elif(dn==3):
##        mn= "March
##    elif(dn==4):
##        mn= "April"
##    elif(dn==5):
##        mn= "May"
##    elif(dn==6):
##        mn= "Jun"
##    elif(dn==7):
##        mn= "July"
##    elif(dn==8):
##        mn= "Augest"
##    elif(dn==9):
##        mn= "September"
##    elif(dn==10):
##        mn= "Octomber"
##    elif(dn==11):
##        mn= "November"
##    elif(dn==12):
##        mn= "December"
##    else:
##        mn= "invalid"
##    return mn


##for i in range(12):
##    inpNum=int(input())
##    print(Month(inpNum))
