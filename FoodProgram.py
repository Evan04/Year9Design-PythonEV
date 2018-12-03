import tkinter as tk

def submit():
	print("Submit pressed")
	list.append(entA.get())
	list.append(entB.get())
	list.append(entC.get())
	print(list)

root = tk.Tk()
root.title("Food Tracker")

list = []


#**************** LABELS 1, 2, 3, 4, 5, 6 *******************

label = tk.Label(root, text = "The average male needs 2500 calories per day.")
label.grid(row = 0, column = 0, columnspan = 2)

label = tk.Label(root, text = "The average female needs 2000 calories per day.")
label.grid(row = 1, column = 0, columnspan = 2)

label = tk.Label(root, text = "Date")
label.grid(row = 0, column = 2, columnspan = 2)

label = tk.Label(root, text = "Quantity - Food Item")
label.grid(row = 2, column = 0, columnspan = 1)

label = tk.Label(root, text = "Calories")
label.grid(row = 2, column = 2, columnspan = 2)

label = tk.Label(root, text = "                  ")
label.grid(row = 4, column = 1, columnspan = 5)

#***************** ENT 1, 2, 3 ***********************

entA = tk.Entry(root)
entA.grid(row = 1, column = 2, columnspan = 1)
#Where you input the date (ex. Nov 28, 2018)

entB = tk.Entry(root)
entB.grid(row = 3, column = 0, columnspan = 1)
#Where you input the Quantity - Food Item (ex. 1 banana)

entC = tk.Entry(root)
entC.grid(row = 3, column = 2, columnspan = 1)
#This is where you input your calories at the end of the day

#***************** Button 1 **********************

btn = tk.Button(root, text = "Submit", command = submit)
btn.grid (row = 4, column = 1)




root.mainloop()