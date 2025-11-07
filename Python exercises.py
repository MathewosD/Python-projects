print("Hello!")
def tempchange():
 n=int(input("Give me a number."))
 u1=input("What do you want to convert from?(celsius or fahrenheit)")
 if u1=="celsius":
  nf=((n-32)*5/9,"degrees fahrenheit")
  print(nf)
 elif u1=="fahrenheit":
  nf=(n*9/5+32,"degrees celsius")
  print(nf)
def lengthchange():
 n=int(input("Give me a number"))
 u1=input("What is the unit?(m or ft)?")
 if u1=="m":
  uf=(u1*3.28,"ft")
  print(uf)
 elif u1=="ft":
  uf=(u1/3.28,"m")
  print(uf)
c=input("What do you want to convert Celsius-Fahrenheit(press 1) or meter-feet(press 2)?")
if c=="1":
 tempchange()
elif c=="2":
 lengthchange()



                                           
