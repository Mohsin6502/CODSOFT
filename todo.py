import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("600x400")
        self.filename = "todo_list.json"
        self.tasks = self.load_tasks()
        
        # Create GUI elements
        self.create_widgets()
        
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self):
        """Add a new task."""
        description = self.task_entry.get()
        due_date = self.due_entry.get() or None
        
        if not description:
            messagebox.showwarning("Input Error", "Task description cannot be empty!")
            return
            
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'due_date': due_date
        }
        self.tasks.append(task)
        self.save_tasks()
        self.task_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)
        self.update_task_list()
        messagebox.showinfo("Success", f"Task added: {description}")
    
    def complete_task(self):
        """Mark selected task as completed."""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task!")
            return
            
        task_id = int(self.task_tree.item(selected[0])['values'][0])
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                self.update_task_list()
                messagebox.showinfo("Success", f"Task {task_id} marked as completed.")
                return
    
    def delete_task(self):
        """Delete selected task."""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task!")
            return
            
        task_id = int(self.task_tree.item(selected[0])['values'][0])
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                self.update_task_list()
                messagebox.showinfo("Success", f"Task {task_id} deleted: {deleted_task['description']}")
                return
    
    def update_task_list(self):
        """Update the task list display."""
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
            
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            due = task['due_date'] if task['due_date'] else ""
            self.task_tree.insert("", tk.END, values=(task['id'], status, task['description'], due))
    
    def create_widgets(self):
        """Create and layout GUI widgets."""
        # Input frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X)
        
        ttk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = ttk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=0, column=2, padx=5, pady=5)
        self.due_entry = ttk.Entry(input_frame, width=15)
        self.due_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(input_frame, text="Add Task", command=self.add_task).grid(row=0, column=4, padx=5, pady=5)
        
        # Task list
        columns = ("ID", "Status", "Description", "Due Date")
        self.task_tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.task_tree.heading("ID", text="ID")
        self.task_tree.heading("Status", text="Status")
        self.task_tree.heading("Description", text="Description")
        self.task_tree.heading("Due Date", text="Due Date")
        self.task_tree.column("ID", width=50)
        self.task_tree.column("Status", width=50)
        self.task_tree.column("Description", width=300)
        self.task_tree.column("Due Date", width=100)
        self.task_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Buttons frame
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="Complete Task", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        
        # Initial update
        self.update_task_list()

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()