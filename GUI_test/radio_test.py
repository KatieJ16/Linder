from Tkinter import * 
master = Tk()

v=IntVar()

Radiobutton(master, text="One", variable=v, value=1).pack(anchor=w)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=w)

mainloop()
