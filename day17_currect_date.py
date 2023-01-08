import datetime
ob=datetime.datetime.now()


str1=str(ob.day)+'-'+str(ob.month)+'_'+str(ob.year)
str2=str(ob.hour)+'-'+str(ob.minute)+'-'+str(ob.second)
str3='Backup_'+str1+'_'+str2+'.db'
print(str3)
