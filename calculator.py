import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a tkinter window
window = tk.Tk()
window.title("Calculator")

# Create an entry field
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Create a Clear button
tk.Button(window, text='Clear', padx=20, pady=20, command=clear).grid(row=row_num, column=col_num)

window.mainloop()
