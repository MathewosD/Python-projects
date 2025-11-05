def taxcalc():
  inc=int(input("What is your income?"))
  if 0<=inc<=2000:
        print("You are exempt from tax!")
  elif 2001<=inc<=4000:
      tax=(inc*15/100)
      print("You have to pay a tax of",tax)
      ninc=(inc-tax)
      print("Your net income is",ninc)
  elif 4001<=inc<=7000:
      tax=(tax*20/100)
      print("You have to pay a tax of",tax)
      ninc=(inc-tax)
      print("Your net income is",ninc)
  elif 7001<=inc<=10000:
      tax=(inc*25/100)
      print("You have to pay a tax of",tax)
      ninc=(inc-tax)
      print("Your net income is",ninc)
  elif 10001<=inc<=14000:
      tax=(inc*30/100)
      print("You have to pay a tax of",tax)
      ninc=(inc-tax)
      print("Your net income is",ninc)
  elif 14000<=inc:
      tax=(inc*35/100)
      print("You have to pay a tax of",tax)
      ninc=(inc-tax)
      print("Your net income is",ninc)
taxcalc ()
