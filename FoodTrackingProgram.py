import tkinter as Food Tracking Program

def submit():
	print("Submit pressed")
	list.append(ent.get())
	print(list)
	lab.config(text = "Food Item")

list = []

root = tk.Tk()

lab = tk.Label(root, text = "Input Food")
lab.pack()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text = "Submit", command = submit)
btn.pack()

root.mainloop()