To-Do List Application

Overview:-
This is a simple command-line to-do list application written in Python.
The application allows users to manage tasks by displaying them, adding new tasks, removing tasks, marking tasks as completed, and exiting the application.
Task information such as description, priority, due date, and completion status is stored in a JSON file.

Getting Started:-
To use the to-do list application, follow these steps:

Clone or download the repository.
Make sure you have Python installed on your system.
Run the to_do_list.py file using the command python to_do_list.py in your terminal.

Commands:-
The application provides the following commands in the command menu:

Display Tasks: View the list of tasks along with their details.
Add Task: Add a new task by providing a description, priority (high/medium/low), and due date (optional).
Remove Task: Remove a task by specifying its index in the displayed task list.
Mark Task as Completed: Mark a task as completed by specifying its index in the displayed task list.
Exit: Save tasks and exit the application.
Task Structure
Each task has the following attributes:

Description: A brief description of the task.
Priority: Priority level of the task (high/medium/low).
Due Date: The date by which the task should be completed (optional).
Completed: Indicates whether the task has been completed or not.
Data Storage
Tasks are stored in a JSON file named tasks.json. The file is automatically created and updated as tasks are added, removed, or marked as completed.

Notes:-
Due dates should be entered in the format "YYYY-MM-DD."
The application will continue running until the user chooses to exit.
Feel free to use and modify this to-do list application based on your needs!






