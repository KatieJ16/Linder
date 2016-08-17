import time
from Tkinter import *

root = Tk()

box = Listbox(root)
box.insert(END, 'hello')
box.pack()

root.mainloop()
for i in range(10):
    box.insert(END, i)
    #time.sleep(.1)

