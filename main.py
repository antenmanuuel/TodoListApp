import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

class TodoListApplication:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title('To-Do List Application')

        # Frame for New Task Entry
        self.task_entry_frame = ttk.Frame(self.main_window)
        self.task_entry_frame.pack(padx=10, pady=10, fill='x')

        # Entry Field for Task Description
        self.description_entry = ttk.Entry(self.task_entry_frame, width=50)
        self.description_entry.pack(side='top', fill='x', padx=5, pady=5)

        # Category Selection for Task
        self.task_category = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.task_entry_frame, textvariable=self.task_category,
                                              values=('Work', 'Personal', 'Shopping', 'Other'))
        self.category_combobox.pack(side='top', fill='x', padx=5, pady=5)
        self.category_combobox.current(0)  # Default to 'Work'

        # Detailed Description Text Field
        self.detailed_description_text = tk.Text(self.task_entry_frame, height=5, width=50)
        self.detailed_description_text.pack(side='top', fill='x', padx=5, pady=5)

        # Priority Level Selection
        self.task_priority = tk.StringVar()
        self.priority_combobox = ttk.Combobox(self.task_entry_frame, textvariable=self.task_priority,
                                              values=('Low', 'Medium', 'High'))
        self.priority_combobox.pack(side='top', fill='x', padx=5, pady=5)
        self.priority_combobox.current(1)  # Default to 'Medium'

        # Task Due Date Picker
        self.due_date_calendar = Calendar(self.task_entry_frame, selectmode='day', year=datetime.now().year,
                                          month=datetime.now().month, day=datetime.now().day)
        self.due_date_calendar.pack(side='top', fill='x', padx=5, pady=5)

        # Button to Add Task
        self.add_task_button = ttk.Button(
            self.task_entry_frame, text='Add Task', command=self.add_task)
        self.add_task_button.pack(side='top', fill='x', padx=5, pady=5)

        # List Box for Current Tasks
        self.current_tasks_listbox = tk.Listbox(
            self.main_window, height=10, width=75)
        self.current_tasks_listbox.pack(padx=10, pady=10, fill='x')

        # Button to Mark Task as Complete
        self.complete_task_button = ttk.Button(
            self.main_window, text='Mark Complete', command=self.mark_task_complete)
        self.complete_task_button.pack(padx=10, pady=5, fill='x')

        # List Box for Completed Tasks
        self.completed_tasks_listbox = tk.Listbox(
            self.main_window, height=10, width=75)
        self.completed_tasks_listbox.pack(padx=10, pady=10, fill='x')

        # Button to Remove Completed Task
        self.remove_completed_button = ttk.Button(
            self.main_window, text='Remove Completed', command=self.remove_completed_task)
        self.remove_completed_button.pack(padx=10, pady=5, fill='x')

    def add_task(self):
        description = self.description_entry.get()
        detailed_description = self.detailed_description_text.get("1.0", tk.END).strip()
        category = self.task_category.get()
        priority = self.task_priority.get()
        due_date = self.due_date_calendar.get_date()
        if description:
            task_details = f'[{category}] {description} - Priority: {priority} - Due Date: {due_date} - Details: {detailed_description}'
            self.current_tasks_listbox.insert(tk.END, task_details)
            self.description_entry.delete(0, tk.END)  
            self.detailed_description_text.delete("1.0", tk.END)

    def mark_task_complete(self):
        selected_indices = self.current_tasks_listbox.curselection()
        for index in selected_indices:
            task_detail = self.current_tasks_listbox.get(index)
            self.completed_tasks_listbox.insert(tk.END, task_detail)
        for index in reversed(selected_indices):
            self.current_tasks_listbox.delete(index)

    def remove_completed_task(self):
        selected_indices = self.completed_tasks_listbox.curselection()
        for index in reversed(selected_indices):
            self.completed_tasks_listbox.delete(index)


# Create the Main Window and Run the Application
main_window = tk.Tk()
todo_list_app = TodoListApplication(main_window)
main_window.mainloop()
