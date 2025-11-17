print("Hello user!")

tasks=["Study for History exam", "Study for math exam","Read The River Between"]
print("Here are your tasks for today:", tasks)
def change():
  print("Enter 1 to add a task, enter 2 to remove a task, and enter 3 to clear")
  c=int(input("Enter:"))
  if c==1:
    nv=input("What do you want to add?")
    tasks.append(nv)
    print("Here is the new to-do list:",tasks)
  elif c==2:
    rv=input("What do you want to remove?")
    tasks.remove(rv)
    print("Here is the new to-do list:",tasks)
  elif c==3:
    tasks.clear()
    print("Here is the new to-do list:",tasks)
while True:
  change()


