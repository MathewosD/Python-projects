print("Give me a number.")
while True:
 try:
  n=int(input())
  if n>0:
   print(n,"is a positive number.")
  elif n==0:
   print(n,"is neither positive nor negative.")
  else:
   print(n," is a negative number.")
  break
 except ValueError:
  print("Please write a number.")
