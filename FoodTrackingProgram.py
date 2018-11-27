import tkinter as tk

def submit():
	print("Submit pressed")
	list.append(ent.get())
	print(list)
	lab.config(text = "Food Item")

list = []

root = tk.Tk()
root.title("Food Tracker")

label = tk.Label(root, text = "Quantity - Food Item")
label.pack()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text = "Submit", command = submit)
btn.pack()


#*******************WIDGET 1,2,3,4 (Labels)********************
labInput1 = tk.Label(root. text = "The average male needs 2500 calories per day. The average female needs 2000 calories per day.")
labInput1.grid(row = 0, column = 0)

LabInput2 = tk.Label(root, text = "Date")
LabInput2.grid(row = 1, column = 0)

LabInput3 = tk.Label(root, text = "Quantity - Food Item")
LabInput3.grid(row = 0, column = 1)

LabInput4 = tk.Label(root, text = "Calories")
LabInput4.grid(row = 2, column = 1)


root.mainloop()