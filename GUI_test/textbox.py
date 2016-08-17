from Tkinter import *
root = Tk()
def foo():
    print "Alex"
CA = Label(root, text = "foo")
button = Button(root, text = "Alex", command = foo)
CA.pack()
button.pack()
root.mainloop()
