import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} (Priority: {task['priority']}, Due: {task['due_date']}) {'[Completed]' if task['completed'] else ''}")

def add_task(tasks, description, priority, due_date):
    new_task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    print("Task added successfully.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task['description']}")
    else:
        print("Invalid task index.")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nCommand Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
            add_task(tasks, description, priority, due_date)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
