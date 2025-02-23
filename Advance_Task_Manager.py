import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from datetime import datetime

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "Completed" if task["completed"] else "Pending"
            task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')
    else:
        messagebox.showwarning("Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x600")
root.config(bg="#F7F7F7")

# Create frames for better organization
frame_top = tk.Frame(root, bg="#F7F7F7")
frame_top.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#F7F7F7")
frame_buttons.pack(pady=20)

frame_search = tk.Frame(root, bg="#F7F7F7")
frame_search.pack(pady=10)

frame_list = tk.Frame(root, bg="#F7F7F7")
frame_list.pack(pady=10)

# Task input section
task_label = tk.Label(frame_top, text="Enter a task:", font=("Arial", 14), bg="#F7F7F7")
task_label.grid(row=0, column=0, padx=10, pady=5)

task_entry = tk.Entry(frame_top, width=40, font=("Arial", 12))
task_entry.grid(row=0, column=1, padx=10, pady=5)

# Add task button with custom styling
add_button = tk.Button(frame_buttons, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12), relief="solid", width=20)
add_button.grid(row=0, column=0, padx=10, pady=5)

# Delete task button
delete_button = tk.Button(frame_buttons, text="Delete Task", command=delete_task, bg="#FF5733", fg="white", font=("Arial", 12), relief="solid", width=20)
delete_button.grid(row=0, column=1, padx=10, pady=5)

# Complete task button
complete_button = tk.Button(frame_buttons, text="Complete Task", command=complete_task, bg="#2196F3", fg="white", font=("Arial", 12), relief="solid", width=20)
complete_button.grid(row=1, column=0, padx=10, pady=5)

# Clear all tasks button
clear_button = tk.Button(frame_buttons, text="Clear All Tasks", command=clear_all_tasks, bg="#FFC107", fg="black", font=("Arial", 12), relief="solid", width=20)
clear_button.grid(row=1, column=1, padx=10, pady=5)

# Search section
search_label = tk.Label(frame_search, text="Search tasks:", font=("Arial", 14), bg="#F7F7F7")
search_label.grid(row=0, column=0, padx=10, pady=5)

search_entry = tk.Entry(frame_search, width=40, font=("Arial", 12))
search_entry.grid(row=0, column=1, padx=10, pady=5)

search_button = tk.Button(frame_search, text="Search", command=search_tasks, bg="#9C27B0", fg="white", font=("Arial", 12), relief="solid", width=20)
search_button.grid(row=0, column=2, padx=10, pady=5)

# Task listbox
task_listbox = tk.Listbox(frame_list, width=80, height=15, font=("Arial", 12), bg="#E8F5E9", selectmode=tk.SINGLE)
task_listbox.pack()

# Start the main loop
root.mainloop()