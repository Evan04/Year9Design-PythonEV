import tkinter as tk

root = tk.Tk()
root.title("Food Tracker")

list = []

#****************WIDGET 1,2,3,4 (Labels)*******************

label = tk.Label(root, text = "The average male needs 2500 calories per day.")
label.grid(row = 0, column = 0, columnspan = 1)

label = tk.Label(root, text = "The average female needs 2000 calories per day.")
label.grid(row = 1, column = 0, columnspan = 1)

root.mainloop()