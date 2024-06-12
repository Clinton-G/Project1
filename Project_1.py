tasks = [{'name': 'Dishes', 'status': 'Incomplete'}, {'name': 'Laundry', 'status': 'Incomplete'}]

while True:
    print('''
   Menu:
----------
0: Quit
1: Add a Task
2: View Tasks
3: Mark a Task as Complete
4: Delete a Task
''')
    
    menu_choice = input("Enter choice: ")

    if menu_choice == '0':
        print('Program Ended, Have a Nice Day!')
        break


    elif menu_choice == '1':
        new_task = input("Enter Task: ")
        tasks.append({'name': new_task, 'status': 'Incomplete'})
        print(new_task, "has been added!")

    elif menu_choice == '2':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task['name']} - {task['status']}")


    elif menu_choice == '3':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task['name']} - {task['status']}")
        task_index = int(input("Enter Task You Wish to Mark Completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['status'] = 'Complete'
            print("Task Marked as Complete.")
        else:
            print("Invalid Input, Try Again")


    elif menu_choice == '4':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task['name']} - {task['status']}")
        task_index = int(input("Enter Task to Delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task Deleted.")
        else:
            print("Invalid Input, Try Again")    
    
    else:
        print("Invalid Imput, Try Again")