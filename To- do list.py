#Create a list 
to_do_list = []

#Check if there is any file called("tasks.json")
try:
    with open("tasks.json", "r") as file:
        to_do_list = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    to_do_list = []

#Save the tasks
def save_tasks():
    with open("tasks.json", "w") as f:
        for task in to_do_list:
            f.write(task + "\n")

#Define a function to add a task
def add_task():
        print("")
        print("Alright, enter your task!")
        print("")
        add_task_user = input("Enter a task: ").strip() #Enter the task
        if add_task_user: 
            to_do_list.append(add_task_user) #Works only if a task is added, else not
            print("")
            print(f"Task {add_task_user} added!")
        else:
            print("Task cannot be empty!") 

#Define a function to view a task
def view_task(): 
        if not to_do_list:
            print("You have no tasks! Congrats!") #If there is nothing in the list, then the same prints
        else: #Otherwise, the list prints
            print("\nHere are your tasks!")
            for index, task in enumerate(to_do_list, start = 1): #Index in the to_do_list starts with 1, and task is the task to be done
                print(f"{index}. {task}")

#Define a function to complete a task
def complete_task():
        if len(to_do_list) == 0:
            print("You got no tasks to do!") #If the kength of to_do_list is 0 (or the list is empty), then the same prints
            return
        print("Which task did you complete?\n") #Otherwise, the below code happens
        for index, task in enumerate(to_do_list, start = 1):
            print(f"{index}. {task}")
        try:
            completed_index = int(input("Enter the task number!: ")) - 1
            if 0 <= completed_index < len(to_do_list):
                completed_task = to_do_list.pop(completed_index)
                print(f"Task {completed_task} marked as complete and removed from the list!")
            else:
                print("Invalid task number!")
                return
        except ValueError:
            print("Enter a valid task number!")
            return

#Remove a task
def remove_task():
            if len(to_do_list) == 0:
                print("You have no tasks!")
                return
            for index, task in enumerate(to_do_list, start = 1):
               print(f"{index}. {task}")
            try:
                remove_index = int(input("Enter the task to remove: ")) - 1
                if 0 <= remove_index < len(to_do_list):
                    removed_task = to_do_list.pop(remove_index)
                    print(f"Task \"{removed_task}\" removed!")
                else:
                    print("Invalid task number!")
                    return
            except ValueError:
                print("Enter a valid task number!")
                return

#Game loop
game_running = True
while game_running:
    print("")

    print("Welcome to the To-Do List App!")
    print("1. Add a task\n2. View Tasks\n3. Complete a task\n4. Remove a task\n5. Exit")
    print("")
    try:
        user_view_choice = int(input("Enter your choice!:  "))
    except ValueError:
        print("Please enter a valid choice!")
        continue

    if user_view_choice not in range(1, 6):
        print("Invalid choice!")
    elif user_view_choice == 1:
        add_task()
    elif user_view_choice == 2:
        view_task()
    elif user_view_choice == 3:
        complete_task()
    elif user_view_choice == 4:
        remove_task()
    else:
        save_tasks()
        print("Goodbye")
        print("")
        print("The program ended!")
        