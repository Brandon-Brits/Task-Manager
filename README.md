# Task-Manager

This programme is designed for a small business, in which it will help assist the business to manage tasks that are assigned to each member. All the information will be written to two different text files named **user.txt** and **tasks.txt**.

## What the different txt files will contain:

After the programme is run, the following will be made available to the user in the txt file.

* **tasks.txt** stores a list of all the tasks that the team is working on. The
  information is stored in the text file in the following order:
  
  * The username of the person to whom the task is assigned.
  * The title of the task.
  * A description of the task.
  * The date that the task was assigned to the user.
  * The due date for the task.
  * Either a 'Yes' or 'No' value that specifies if the task has been completed yet.
  
* **user.txt** stores the username and password for each user that has permission to
  use the program. The information is stored in the text file in the following order: 
  
  * First, the username followed by a comma, a space and then the password.
  * One username and corresponding password per line.

## The program allows for the users to do the following:

* Login. The user is prompted to enter a username and password. 
  * If the user is not registered or the username/password is incorrect, an error 
    message will be prompted to the user and will ask the user to try again.
* Statistics. If the logged in user is an admin, the statistics option will be 
  shown to the user, which shows all the information from the generate reports
  function.
* Generate reports. If the logged in user is an admin and the generate reports 
  function is selected, two text files, called **task_overview.txt** and 
  **user_overview.txt** will be generated and display the following:
  * **task_overview.txt** will display:
   1. The total number of tasks that have been generated and tracked.
   1. The total number of completed tasks.
   1. The total number of uncompleted tasks.
   1. The total number of tasks that haven't been completed and that are overdue.
   1. The percentage of tasks that are incomplete.
   1. The percentage of tasks that are overdue.
   
  * **user_overview.txt** will display:
   1. The total number of users registered.
   1. The total number of tasks that have been generated and tracked.
   1. For each user in the database, the total number of tasks assigned to each 
      user, the percentage of the total number of tasks that has been assigned
      to each user, the percentage of the complete, incompleted and overdue
      tasks that has been assigned to each user.
      
* Register user. If the logged in user is an admin, the admin user will be prompted
  for a new username and password and then confirmation of the password, which will 
  then be added to the **user.txt** file.
* Add task. The user is prompted to enter the username of the person the task is 
  assigned to, the title of the task, a description of the task and the due date 
  of the task. The current date will automatically be added aswell. All the 
  information will be written to **tasks.txt**.
 * View all. All tasks that has been written to the txt file will be shown to the 
   user in an easy-to-read format.
 * View mine. All the tasks of the logged-in user will be displayed or if the 
   user decides to select a specific task to mark the task as complete or edit
   the task, he or she can select the number of the task number, the user can
   otherwise type '-1' to return to the main menu.
