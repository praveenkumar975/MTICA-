'''OUTPUT:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}'''


dic1={'Ten':10,'Twenty':20,'Thirty':30}
dic2={'Thirty':30,'Fourty':40,'Fifty':50}

dic3={**dic1,**dic2}
print(dic3)
