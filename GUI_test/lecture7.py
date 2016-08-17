#!/usr/bin/python

from Tkinter import *
import time

def Insert():
    name = text.get()
    name2 = text2.get()

    list.insert(END, name)
    time.sleep(2)
    list.insert(END, name2)
    text2.delete(0,END)
    text.delete(0,END)
    print 'done with Insert()'

root = Tk()
root.geometry('200x210+350+70')

text = Entry(root, bg = 'white')
text2 = Entry(root, bg = 'white')

button = Button(root, text = 'press me', command = Insert)

list = Listbox(root, bg = 'blue', fg = 'yellow')

text.pack()
text2.pack()

button.pack(padx = 4, pady = 4, anchor = E)

list.pack()
print 'pack'

root.mainloop()
print 'DONE()'
