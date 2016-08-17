from Tkinter import *
root = Tk()

li = 'Carl Patrick Lindsay Helmut Chris Gwen'.split()
listb = Listbox(root)
for item in li:
    listb.insert(0,item)

listb.pack()
root.mainloop()
