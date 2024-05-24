import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the list
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"[Completed] {task}")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to complete.")

# Function to save tasks to a file
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    if tasks:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(f"{task}\n")
    else:
        messagebox.showwarning("Warning", "No tasks to save.")

# Function to load tasks from a file
def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        tasks_listbox.delete(0, tk.END)
        with open(file_path, 'r') as file:
            for line in file:
                tasks_listbox.insert(tk.END, line.strip())

# Set up the main application window
app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x400")
app.config(bg="#F0F0F0")

# Create and place widgets
frame = tk.Frame(app, bg="#F0F0F0")
frame.pack(pady=20)

task_entry = tk.Entry(frame, width=40, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

tasks_listbox = tk.Listbox(app, width=50, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

button_frame = tk.Frame(app, bg="#F0F0F0")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

complete_button = tk.Button(button_frame, text="Complete Task", width=15, command=complete_task)
complete_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(button_frame, text="Save Tasks", width=15, command=save_tasks)
save_button.grid(row=1, column=0, padx=10, pady=10)

load_button = tk.Button(button_frame, text="Load Tasks", width=15, command=load_tasks)
load_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter event loop
app.mainloop()
