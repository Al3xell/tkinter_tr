# -*- coding: utf-8 -*-
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    import tkinter as tk
    from tkinter import filedialog 

class Menubar(tk.Frame):
    def __init__(self,parent=None):
        tk.Frame.__init__(self, borderwidth=2)
        if parent :
            self.parent=parent
            menu=tk.Menu(parent)
            parent.config(menu=menu)
            fileMenu=tk.Menu(menu)
            #menu.add_cascade(label="File",menu=fileMenu)
            menu.add_cascade(label="File",underline=0,menu=fileMenu)
            #fileMenu.add_command(label="Save",command=self.save)
            fileMenu.add_command(label="Save",accelerator="Ctrl-S", command=self.save)
            fileMenu.add_separator()
            fileMenu.add_command(label="Exit", command=self.close_app)
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="About Us ...",command=self.about_us)
            menu.add_cascade(label="Help", menu=fileMenu)
            self.bind_all("<Control-S>",self.save)

    def save(self,event=None):
        formats=[('Texte','*.py'),('Portable Network Graphics','*.png')]
        filename=filedialog.asksaveasfilename(parent=self,filetypes=formats,title="Save...")
        if len(filename) > 0:
            print("Sauvegarde en cours dans %s" % filename)

    def close_app(self):
        exit()

    def about_us(self):
        print("about_us %s" % "Nom-Prenom")
        
if __name__ == "__main__" :
    mw = tk.Tk()
    app = Menubar(mw)
    mw.wm_title("Tkinter : Menubar")
    mw.mainloop()

