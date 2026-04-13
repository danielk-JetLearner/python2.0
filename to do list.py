task=[]
while True:
    print("1.View tasks")
    print("2.Add a task")
    print("3.Remove a task")
    print("4.Exit")
    option = int(input("which option"))
    if option == 1:
        print(task)
    elif option == 2:
        assignment = input("what task would you like to add.")
        task.append(assignment)
    elif option == 3:
        assignment = input("What task would you like to delete.")
        task.remove(assignment)  
    elif option == 4:
        break  
    
