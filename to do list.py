import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Create and configure the task list
        self.task_listbox = tk.Listbox(master, width=40)
        self.task_listbox.pack(padx=10, pady=10)

        # Create and configure the entry for new tasks
        self.new_task_entry = tk.Entry(master, width=30)
        self.new_task_entry.pack(pady=5)

        # Create buttons for actions
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)
        
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.new_task_entry.get()
            if updated_task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.new_task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")
        else:
            messagebox.showwarning("Warning", "Select a task to update.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Select a task to remove.")

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
