import tkinter as tk
from tkinter import messagebox
# Expense data structure
expenses = []

# Function to add expenses
def add_expense():
    try:
        date = date_entry.get()
        amount = float(amount_entry.get())
        category = category_var.get()
        description = description_entry.get()

        # Basic validation for required fields
        if not all([date, amount, category]):
            raise ValueError("Please fill in all required fields.")

        # Create an expense dictionary
        expense = {"date": date, "amount": amount, "category": category, "description": description}
        expenses.append(expense)

        # Clear entry fields for next input
        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        category_var.set(category_options[0])  # Reset category to first option
        description_entry.delete(0, tk.END)

        display_expenses()  # Update expense list after adding

        tk.messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))

# Function to display expenses in a listbox
def display_expenses():
    expense_list.delete(0, tk.END)  # Clear existing list items

    for expense in expenses:
        expense_list.insert(tk.END, f"{expense['date']} - {expense['amount']} ({expense['category']}) - {expense['description']}")

# Function to clear all expenses
def clear_expenses():
    expenses.clear()
    display_expenses()  # Update expense list after clearing
    tk.messagebox.showinfo("Success", "Expenses cleared successfully!")

# Main program
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")  # Set window size

# Light blue background
root.configure(bg="#d0e0e0")

# Font style for labels and entries
font_style = ("Arial", 12)

# Date entry
date_label = tk.Label(root, text="Date:", font=font_style)
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
date_entry = tk.Entry(root, width=20, font=font_style)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Amount entry
amount_label = tk.Label(root, text="Amount:", font=font_style)
amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
amount_entry = tk.Entry(root, width=20, font=font_style)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Category selection
category_label = tk.Label(root, text="Category:", font=font_style)
category_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

category_var = tk.StringVar(root)
category_options = ["Select category","Food", "Transportation", "Entertainment", "Other"]
category_var.set(category_options[0])
# Apply font style to individual widgets within OptionMenu
category_dropdown = tk.OptionMenu(
    root, category_var, *category_options
)
category_dropdown["menu"].configure(font=font_style)
category_dropdown.grid(row=2, column=1, padx=5, pady=5)


# Description entry
description_label = tk.Label(root, text="Description:", font=font_style)
description_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
description_entry = tk.Entry(root, width=20, font=font_style)
description_entry.grid(row=3, column=1, padx=5, pady=5)

# Add expense button with light green background
add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense,
    font=font_style,
    bg="#90EE90",  # Light green background
)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Expense listbox with heading and scrollbar
expense_list_label = tk.Label(root, text="Expenses:", font=font_style)
expense_list_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

expense_list = tk.Listbox(root, width=50, font=font_style)
expense_list.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=expense_list.yview)
scrollbar.grid(row=6, column=2, sticky="nsew")
expense_list.configure(yscrollcommand=scrollbar.set) 

# Clear expenses button
clear_button = tk.Button(root, text="Clear Expenses", command=clear_expenses, font=font_style)
clear_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)



# Run the main loop
display_expenses() 
root.mainloop()

