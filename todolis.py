import tkinter as tk

# Function to add a new task
def add_task():
  task = task_entry.get()
  if task != "":
    tasks_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)  # Clear entry field after adding
  else:
    # Show message if no task entered
    tk.messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task
def delete_task():
  selected_item = tasks_list.curselection()
  if selected_item:
    tasks_list.delete(selected_item[0])  # Delete task at selected index
  else:
    # Show message if no task selected
    tk.messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a label for the task entry
task_label = tk.Label(window, text="Enter task:")
task_label.pack()

# Create an entry field for adding tasks
task_entry = tk.Entry(window)
task_entry.pack()

# Create a button to add tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
tasks_list = tk.Listbox(window, width=50)
tasks_list.pack()

# Create a button to delete tasks
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the main event loop
window.mainloop()
