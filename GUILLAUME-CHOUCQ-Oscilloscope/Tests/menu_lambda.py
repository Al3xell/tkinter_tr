from tkinter import *

root = Tk()

def hello(param):
    print(param)

# create a toplevel menu
menubar = Menu(root)
x,y=1,2
menubar.add_command(label="Hello!", command=lambda x=1: hello(x))
menubar.add_command(label="Quit!", command=lambda x=2: hello(x))


# display the menu
root.config(menu=menubar)

mainloop()