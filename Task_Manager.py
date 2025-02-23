import sys
import os
import json
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

tasks = []

TASKS_FILE = "tasks.json"


def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        print(Fore.GREEN + "Tasks loaded successfully.")
    else:
        print(Fore.YELLOW + "No previous tasks found. Starting fresh!")


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    print(Fore.GREEN + "Tasks saved successfully.")


def add_task(task):
    task_details = {"task": task, "completed": False, "due_date": None}
    tasks.append(task_details)
    print(Fore.CYAN + f"Task added: {task}")


def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(Fore.RED + f"Task deleted: {removed_task['task']}")
    except IndexError:
        print(Fore.RED + "Invalid task number")


def view_tasks():
    if not tasks:
        print(Fore.YELLOW + "No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            due_date = f"Due: {task['due_date']}" if task["due_date"] else "No due date"
            print(f"{Fore.MAGENTA}{i + 1}. {task['task']} [{status}] {Fore.WHITE}- {due_date}")


def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(Fore.GREEN + f"Task marked as completed: {tasks[task_index]['task']}")
    except IndexError:
        print(Fore.RED + "Invalid task number")


def set_due_date(task_index, due_date):
    try:
        tasks[task_index]["due_date"] = due_date
        print(Fore.YELLOW + f"Due date set for task: {tasks[task_index]['task']} to {due_date}")
    except IndexError:
        print(Fore.RED + "Invalid task number")


def show_help():
    print(Fore.BLUE + """
    Available commands:
    - add <task>: Add a new task
    - delete <task_number>: Delete a task by its number
    - view: View all tasks
    - complete <task_number>: Mark a task as completed
    - due <task_number> <date>: Set a due date for a task (format: YYYY-MM-DD)
    - help: Show this help message
    - exit: Exit the application
    """)


def main():
    print(Fore.GREEN + "Welcome to the Task Manager Application!\n")
    load_tasks()
    show_help()

    while True:
        command = input(Fore.YELLOW + "Enter command: ").strip().split()
        if not command:
            continue

        if command[0] == "add":
            add_task(" ".join(command[1:]))
        elif command[0] == "delete":
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print(Fore.RED + "Invalid command")
        elif command[0] == "view":
            view_tasks()
        elif command[0] == "complete":
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print(Fore.RED + "Invalid command")
        elif command[0] == "due":
            if len(command) > 2 and command[1].isdigit():
                try:
                    due_date = datetime.strptime(command[2], "%Y-%m-%d").date()
                    set_due_date(int(command[1]) - 1, due_date)
                except ValueError:
                    print(Fore.RED + "Invalid date format. Use YYYY-MM-DD.")
            else:
                print(Fore.RED + "Invalid command")
        elif command[0] == "help":
            show_help()
        elif command[0] == "exit":
            save_tasks()
            print(Fore.GREEN + "Exiting the application. Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()