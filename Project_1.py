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
        task_index = int(input("Enter the index of the task to mark as complete: ")) - 1                # Had to find an awnser for 3, couldnt really figure it out at all
        if 0 <= task_index < len(tasks):
            tasks[task_index]['status'] = 'Complete'
            print("Task marked as complete.")
        else:
            print("Invalid task index!")


    elif menu_choice == '4':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task['name']} - {task['status']}")
        task_index = int(input("Enter index of the task: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid Input, Try Again")    
    
    else:
        print("Invalid Imput, Try Again")