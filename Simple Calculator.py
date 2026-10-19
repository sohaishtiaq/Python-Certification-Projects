from tkinter import *
import math

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        Button(root, text=btn, width=5, command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=btn, width=5, command=lambda b=btn: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="C", width=10, command=clear).grid(row=6, column=3)

root.mainloop()
