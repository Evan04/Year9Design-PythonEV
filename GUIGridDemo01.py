#tkinter is a module that holds all the function
#that let us easily make GUI elements
import tkinter as tk

#creating the naim window. To do this
#we need to call the Tk() function
root = tk.Tk()

label = tk.Label(root, text =  "Welcome to Concentration!")
label.grid(row = 0, column = 0, columnspan = 2)


btn1 = tk.Label(root, text =  "?")
btn1.config(width = 5, height = 5)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Label(root, text =  "?")
btn2.config(width = 5, height = 5)
btn2.grid(row = 2, column = 1, sticky = "NESW")

btn3 = tk.Label(root, text =  "?")
btn3.config(width = 5, height = 5)
btn3.grid(row = 3, column = 0, sticky = "NESW")

btn4 = tk.Label(root, text =  "?")
btn4.config(width = 5, height = 5)
btn4.grid(row = 4, column = 1, sticky = "NESW")


#This line displays the root and sets the program
#in an infinit loop. THis is an EVENT DRIVEN PROGRAM
root.mainloop()