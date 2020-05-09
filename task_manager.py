# task_manager
# Brandon Brits
# 22/04/2020
# Task manager 
#################################
import datetime

def reg_user(user_names):
    registered = False
    new_user = open("user.txt","a")
    user_exists = None
    new_username = input("PLEASE ENTER NEW USERNAME: ")
    # Checks if the user exists 
    if new_username in user_names:
        user_exists = True
    while user_exists == True:
        if new_username in user_names:
            print("\nUSER ALREADY IN SYSTEM")
            new_username = input("PLEASE ENTER NEW USERNAME: ")
        else:
            user_exists = False
    # Registers new user 
    while registered == False:
        new_password = input("PLEASE ENTER PASSWORD ")
        new_password_confirm = input("CONFIRM PASSWORD: ")
        if new_password == new_password_confirm:
            new_user.write("\n{}, {}".format(new_username,new_password))
            registered = True
            print("\nNEW USER ADDED")
            new_user.close()
        else:
            print("\nPASSWORD NOT CONFIRMED")
def show_stats():
    # Creates reports
    generate_report()
    # Opens report files
    with open("task_overview.txt","r") as file:
        task_report = file.readlines()   
    with open("user_overview.txt","r") as file:
        user_report = file.readlines()
    # Outputting report files 
    print("\nTASK STATISTICS\n")
    for line in task_report:
        print(line,end = "")
    print("\n\nUSER STATISTICS\n")
    for line in user_report:
        print(line,end = "")
def add_task(user_names):
    task_entered = False
    while task_entered == False:
        task_user = input("\nENTER USER NAME: ")
        if task_user not in user_names:
            print("\nUSER NOT IN SYSTEM")
        else:
            task_title = input("TASK TITLE: ")
            task_descrip = input("DESCRIPTION: ")
            task_due_date = input("DUE DATE: ")
            task_date = datetime.datetime.now().strftime("%d %b %Y")
            task_complete = "No"
            new_task = open("tasks.txt","a")
            new_task.write("\n{}, {}, {}, {}, {}, {}".format(task_user,task_title,
                        task_descrip,task_date,task_due_date,task_complete))
            task_entered = True
            print("\nNEW TASK ADDED")
            new_task.close()
def view_all():
    all_tasks = open("tasks.txt","r")
    num = 1
    for line in all_tasks:
        temp = line.strip()
        temp = temp.split(", ")
        print("")
        print("{}   TASK USER              :{}".format(num,temp[0]))
        print("    TASK NAME              :{}".format(temp[1]))
        print("    DESCRIPTION            :{}".format(temp[2]))
        print("    DATE ASSIGNED          :{}".format(temp[3]))
        print("    DATE DUE               :{}".format(temp[4]))
        print("    COMPLETION STATUS      :{}".format(temp[5]))
        num += 1
    all_tasks.close()
def view_mine(username,user_names):
    with open("tasks.txt","r") as file:
        all_tasks = file.readlines()
    # Users task output
    num = 1
    count = 1
    all_tasks_copy = all_tasks.copy()
    user_tasks = []
    for line in all_tasks:
        temp = line.strip()
        temp = temp.split(", ")
        if username in line:
            print("")
            print("{}   USER                    :{}".format(num,temp[0]))
            print("    TASK                   :{}".format(temp[1]))
            print("    DESCRIPTION            :{}".format(temp[2]))
            print("    DATE ENTERED           :{}".format(temp[3]))
            print("    DUE DATE               :{}".format(temp[4]))
            print("    COMPLETION STATUS      :{}".format(temp[5]))
            user_tasks.append(all_tasks_copy.pop(count - num))
            num += 1
        count += 1    
    all_tasks = all_tasks_copy.copy()
    # Handles selecting task options 
    print("\n* - SELECT TASK BY ITS CORRESBONDING NUMBER")
    print("B - BACK TO MAIN MENU")
    choice = input(": ").upper()
    # Handles choice of option 
    if choice == "B":
        return
    else:
        choice = int(choice) - 1
        if choice > len(user_tasks) - 1:
            print("\nNO TASK HAS THAT NUMBER")
        else:
            if "Yes" in user_tasks[choice]:
                print("\nTHIS TASK IS COMPLETED AND CONNOT BE EDITED")
            else:
                print("\nM - COMPLETE THE TASK")
                print("E - EDIT TASK")
                choice_2 = input(": ").upper()

                if choice_2 == "M":
                    mark_complete(all_tasks,choice,user_tasks)
                elif choice_2 == "E":
                    edit_task(all_tasks,choice,user_names,user_tasks)
def mark_complete(all_tasks,choice,user_tasks):
    user_tasks[choice] = user_tasks[choice].replace("No","Yes")    
    # Adding users array with main array
    all_tasks.extend(user_tasks)   
    # Splitting lines into list
    all_tasks_sorted = []
    for line in all_tasks:
        line = line.split(", ")
        all_tasks_sorted.append(line)
    # Sorts tasks output
    all_tasks_output = []
    all_tasks = sorted(all_tasks_sorted, key = lambda x: datetime.datetime.strptime(x[3],"%d %b %Y"))
    for array in all_tasks:
        array = ", ".join(array)
        all_tasks_output.append(array)
    # Output to tasks.txt
    with open("tasks.txt","w") as file:
        file.writelines(all_tasks_output)
    print("\nTASK IS COMPLETE")
def edit_task(all_tasks,choice,user_names,user_tasks):
    # Input edit user choice
    edit_user_choice = input("\nWOULD YOU LIKE TO EDIT TASKS ASSIGNED TO THIS USER?\nY OR N: ").upper()
    # Handles edit user
    if edit_user_choice == "Y":
        edited_user = input("NEW ASSIGNED USER: ")
        if edited_user not in user_names:
            print("THAT USER DOES NOT EXIST")
        else:
            edit_user(all_tasks,choice,user_names,user_tasks,edited_user)
    # Input edit date choice
    edit_date_choice = input("\nWOULD YOU LIKE TO EDIT THE DUE DATE?\nY OR N: ")
    if edit_date_choice == "Y":
        edit_date(all_tasks,choice,user_names,user_tasks)
def edit_user(all_tasks,choice,user_names,user_tasks,edited_user):
    user_tasks[choice] = user_tasks[choice].split(", ")
    user_tasks[choice][0] = edited_user
    user_tasks[choice] = ", ".join(user_tasks[choice])    
    # Adding users array with main array
    all_tasks_user = []
    all_tasks_user.extend(all_tasks)
    all_tasks_user.extend(user_tasks)
    # Splitting lines into list
    all_tasks_sorted = []
    for line in all_tasks_user:
        line = line.split(", ")
        all_tasks_sorted.append(line)
    # Sorts tasks output
    all_tasks_output = sorted(all_tasks_sorted,
    key = lambda x: datetime.datetime.strptime(x[3],"%d %b %Y"))
    all_tasks_output_user = []
    for array in all_tasks_output:
        array = ", ".join(array)
        all_tasks_output_user.append(array)
    with open("tasks.txt","w") as file:
        file.writelines(all_tasks_output_user)
    print("USER ASSIGNED TO ASK CHANGED")
def edit_date(all_tasks,choice,user_names,user_tasks):
    # Handles edit date
    edited_date = input("NEW DUE DATE: ")
    user_tasks[choice] = user_tasks[choice].split(", ")
    user_tasks[choice][4] = edited_date
    user_tasks[choice] = ", ".join(user_tasks[choice])
    # Adding users array with main array
    all_tasks_date = []
    all_tasks_date.extend(all_tasks)
    all_tasks_date.extend(user_tasks)
    # Splitting lines into list
    all_tasks_sorted = []
    for line in all_tasks_date:
        line = line.split(", ")
        all_tasks_sorted.append(line)
    # Sorts tasks output
    all_tasks_output = sorted(all_tasks_sorted,
    key = lambda x: datetime.datetime.strptime(x[3],"%d %b %Y"))
    all_tasks_output_date = []
    for array in all_tasks_output:
        array = ", ".join(array)
        all_tasks_output_date.append(array)
    with open("tasks.txt","w") as file:
        file.writelines(all_tasks_output_date)
def generate_report():
    # Generates task report
    with open("tasks.txt","r") as file:
        info = file.readlines()
    # Intialising counting variables
    num_of_tasks = 0
    num_of_complete_tasks = 0
    num_of_uncompleted_tasks = 0
    num_of_overdue_tasks = 0
    # Checking through tasks info
    for line in info:
        num_of_tasks += 1
        if "Yes" in line:
            num_of_complete_tasks += 1
        if "No" in line:
            num_of_uncompleted_tasks += 1
        line = line.split(", ")
        due_date = datetime.datetime.strptime(line[4],"%d %b %Y")
        date = datetime.datetime.now()
        line = ", ".join(line)
        if date > due_date:
            num_of_overdue_tasks += 1
    # Working out the percentages   
    percentage_incomplete = (num_of_uncompleted_tasks/num_of_tasks) * 100
    percentage_overdue = (num_of_overdue_tasks/num_of_tasks) * 100
    # Creating report output list
    tasks_report_output = ["TOTAL TASKS\t\t\t:" + str(num_of_tasks) + "\n",
                        "COMPLETED TASKS\t\t\t:" + str(num_of_complete_tasks) + "\n",
                        "INCOMPLETE TASKS\t\t:" + str(num_of_uncompleted_tasks) + "\n",
                        "TASKS OVERDUE\t\t\t:" + str(num_of_overdue_tasks) + "\n",
                        "PERCENTAGE OF INCOMPLETE TASKS\t:" +
                        str(round(percentage_incomplete,1)) + "%\n",
                        "PERCENTAGE OF OVERDUE TASKS\t:" +
                        str(round(percentage_overdue,1)) + "%"]
    # Adding text to the report file
    with open("task_overview.txt","w") as file:
        file.writelines(tasks_report_output)
    # Generates user report 
    # Open file and create user list
    with open("user.txt","r") as file:
        user_info = file.readlines()
    num_users = 0
    users = ""
    for line in user_info:
        num_users += 1
        temp = line.split(", ")
        users += temp[0] + " "
    # Initialising list variables
    users = users.split()
    num_task_user_total_list = []
    num_task_user_list = []
    num_task_user_complete_list = []
    num_task_user_incomplete_list = []
    num_task_user_over_list = []
    # Checking through each users info
    for user in users:
        num_task_user = 0
        num_task_user_complete = 0
        num_task_user_incomplete = 0
        num_task_user_over = 0
        for line in info:
            if user in line:
                num_task_user += 1
                if "Yes" in line:
                    num_task_user_complete += 1 
                if "No" in line:
                    num_task_user_incomplete += 1
                if "No" in line and date > due_date:
                    num_task_user_over += 1
        # Working out each users outputs
        if num_task_user > 0:
            percentage_user = (100/num_of_tasks) * num_task_user
            percentage_user_complete = (100/num_task_user) * num_task_user_complete
            percentage_user_incomplete = (100/num_task_user) * num_task_user_incomplete
            percentage_user_overdue = (100/num_task_user) * num_task_user_over
        else:
            percentage_user = 0
            percentage_user_complete = 0
            percentage_user_incomplete = 0
            percentage_user_overdue = 0
        # Creating lists of users outputs
        num_task_user_total_list.append(num_task_user)
        num_task_user_list.append(percentage_user)
        num_task_user_complete_list.append(percentage_user_complete)
        num_task_user_incomplete_list.append(percentage_user_incomplete)
        num_task_user_over_list.append(percentage_user_overdue)
    # Creating report output list
    user_report_output = ["Total users\t\t\t:" + str(num_users) + "\n",
                        "Total tasks\t\t\t:" + str(num_of_tasks) + "\n",]
    # Creating each users report output list
    each_users_output = []
    count = 0
    for user in users:
        each_users_output.append("\n" + user +
                                "\nTasks assigned\t\t\t:" +
                                str(num_task_user_total_list[count]) +
                                "\nTasks assigned of total tasks\t:" +
                                str(round(num_task_user_list[count],1)) +
                                "%\nTasks assigned completed\t:" +
                                str(round(num_task_user_complete_list[count],1)) +
                                "%\nTasks assigned incomplete\t:" +
                                str(round(num_task_user_incomplete_list[count],1)) +
                                "%\nTasks assigned overdue\t\t:" +
                                str(round(num_task_user_over_list[count],1)) + "%\n"
                                )
        count += 1
    # Adding the text to the report file
    with open("user_overview.txt", "w") as file:
        file.writelines(user_report_output)
    with open("user_overview.txt","a") as file:
        file.writelines(each_users_output)
    # Terminal output
    print("\nREPORT GENERATED")

########################################################################################################
#######################################  PROGRAM STARTUP  ##############################################
########################################################################################################

close = False
login = False
user_names = ""
user_passwords = ""
logged_in = False
# Handles all user options
while close == False:
    # Logging in 
    while logged_in == False:
        users = open("user.txt","r")
        user_names = []
        user_passwords = []
        for line in users:
            temp = line.strip()
            temp = temp.split(", ")
            user_names.append(temp[0])
            user_passwords.append(temp[1])
        users.close()
        print("########## WELCOME ##########")
        print("L - LOGIN")
        print("E - EXIT")
        choice = input(": ").upper()
        if choice == "L":
            while logged_in == False:
                username = input("USERNAME: ")
                password = input("PASSWORD: ")
                if username not in user_names:
                    print("\nTHE USER DOES NOT EXIST")
                elif password not in user_passwords:
                    print("\nTHE PASSWORD ENTERED IS INCORRECT")
                else:
                    logged_in = True
        elif choice == "E":
            close = True
            break
    # Logged in 
    while logged_in == True:
    # Option menu 
        print("\nPLEASE SELECT ONE OF THE OPTIONS: ")
        if username == "admin":
            print("R  - REGISTER NEW USER")
        print("A  - ADD A TASK")
        print("VA  - VIEW ALL TASKS")
        print("VM  - VIEW MY TASKS")
        if username == "admin":
            print("DS  - DISPLAY STATISTICS")
            print("GR  - GENERATE REPORTS")
        print("B  - BACK TO LOGIN")
        option = input(": ").upper()
        # Handles Options 
        # Registers new user
        if option == "R" and username == "admin":
            reg_user(user_names)
        # Adds task
        if option == "A":
            add_task(user_names)
        # All tasks output
        if option == "VA":
            view_all()
        # User's tasks output
        if option == "VM":
            view_mine(username,user_names)
        # Displays stats
        if option == "DS" and username == "admin":
            show_stats()
        # Generates reports 
        if option == "GR" and username == "admin":
            generate_report()
        # Exits Menu
        if option == "B":
            logged_in = False