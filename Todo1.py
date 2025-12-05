print("=== To-Do List===")
todo=["Study history, write bio lab report"]
comp=[]
print(todo)
print("===Completed===")
print(comp)

while True:

  def add_task():
   add=input("What do you want to add?")
   todo.append(add)
  
  def remove_task():
   remove=input("What do you want to remove?")
   if remove in todo:
    todo.remove(remove)
   else:
    print(edit,"is not found in the list.")
  
  def edit_task():
   edit=input("Which task do you want to edit?")
   if edit in todo:
    todo.remove(edit)
    add=input("What will you replace it with?")
    todo.append(add)

   else:
    print(edit,"is not found in the list.")
     
  def mark_as_completed():
    completed=input("Which task did you complete?")
    if completed in todo:
     todo.remove(completed)
     comp.add(completed)
  print("""
  1-Add new task
  2-Remove task
  3-Edit task
  4-Mark task as completed
  5-Exit""")
  choice=input("Enter your choice(1-5)")
  if choice=="1":
    add_task()
  elif choice=="2":
    remove_task()
  elif choice=="3":
    edit_task()
  elif choice=="4":
    mark_as_completed()
  elif choice=="5":
    break
  print("=== To-Do List===")
  p=[]
  print(todo)
  print("===Completed===")
  print(comp)


    

