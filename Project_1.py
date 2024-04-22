# menu = ['0: Quit', '1: Add a Task', '2: View Tasks', '3: Mark a Task as Complete', '4: Delete a Task']
task_list = ['1: Grocery Store - Incomplete', '2: Dishes - Incomplete', '3: Laundry - Incomplete']

menu = print('''
   Menu:
----------
0: Quit
1: Add a Task:
2: View Tasks:
3: Mark a Task as Complete:
4: Delete a Task
''')

menu_choice = input("Enter Input: ")


if menu_choice == '1':
    print(task_list)
    menu_1 = input('''
    Enter Task as Shown Above
''')
    task_list.append(menu_1)
    print(menu_1, 'Has Been Added!')
    menu_2 = input("Would You Like to Add Another Task? ")
    pass


if menu_choice == '2':
    # task_list = print('''
    #   Task List:
    #   ----------
    # 1: Grocery Store - Incompleted
    # 2: Dishes - Complete
    # 3: Laundry - Incomplete
    # 0: Quit
    # ''')
    print(task_list)



task_choice = input("Enter Input: ")




if menu_choice == '3':
    input('Which Task Would You Like to Mark as Completed? ')




if menu_choice == '4':
    task_delete = input('Which Task # Would You Like to Delete? ')
    if task_delete == '1':
        task_list.remove('1: Grocery Store - Incomplete')
    elif task_delete == '2':
        task_list.remove('2: Dishes - Incomplete')
    elif task_delete == '3':
        task_list.remove('3: Laundry - Incomplete')



if menu_choice == '0':
    print('Program Ended, Have a Nice Day! ')