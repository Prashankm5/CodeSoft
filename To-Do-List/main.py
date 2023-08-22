import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_listbox()
        task_entry.delete(0, tk.END)

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_index]["task"] = new_task
            update_task_listbox()

def complete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        tasks[selected_index]["completed"] = True
        update_task_listbox()

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del tasks[selected_index]
        update_task_listbox()

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else " "
        task_listbox.insert(tk.END, f"[{status}] {task['task']}")

root = tk.Tk()
root.title("To-Do List App")

# Background color
root.configure(bg="#F0F0F0")

task_entry = tk.Entry(root, width=40, bg="#E0E0E0")
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#00BFFF", fg="white")
add_button.pack()

task_listbox = tk.Listbox(root, width=40, bg="#E0E0E0")
task_listbox.pack(pady=10)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg="#FFA500", fg="white")
edit_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task, bg="#32CD32", fg="white")
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF0000", fg="white")
delete_button.pack()

update_task_listbox()

root.mainloop()