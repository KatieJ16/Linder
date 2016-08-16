from Tkinter import *

class App:
    
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg='red', command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        v = IntVar()
        Radiobutton(master, text="one", variable=v, value=1).pack(anchor=w)
        Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=w)


    def say_hi(self):
        print"hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional

