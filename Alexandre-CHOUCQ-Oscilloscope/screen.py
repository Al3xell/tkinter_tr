from observer import Observer
from generator import Generator

import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog, messagebox

class Screen(Observer):
 
#-----Constructor-----#
    def __init__(self, parent, bg="white"):
        self.parent=parent
        self.canvas=tk.Canvas(parent,bg=bg)
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))
        self.resize=False
        self.tiles=4

#-----___str___-----#

    def __repr__(self):
        return "Screen()"

    def __str__(self):
        return f'\nScreen : width = {self.width}, height = {self.height}\n'

#-----Getter-----#
    def get_canvas(self) :
        return self.canvas
    
    def get_tiles(self):
        return self.tiles
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def get_parent(self):
        return self.parent
 
#-----Setter-----#

    def set_tiles(self,tiles):
        self.tiles=tiles
#-----Methods-----#

    def plot_signal(self,signal,name="signal",color="red",erase=False):
        width,height=self.width,self.height
        if signal and len(signal)>1:
            self.canvas.delete(name)
            plot=[(x*width, height/2*(y+1)) for (x,y) in signal]
            self.canvas.create_line(plot,fill=color,smooth=1,width=3,tags=name)

    def create_grid(self):
        width,height=self.width,self.height
        tiles=self.tiles
        tile_x=width/tiles
        for t in range(1,tiles+1):          # lignes verticales
            x=t*tile_x
            self.canvas.create_line(x,0,x,height,tags="grid")
            self.canvas.create_line(x,height/2-5,x,height/2+5 ,width=4,tags="grid")
        tile_y=height/tiles
        for t in range(1,tiles+1):        # lignes horizontales
            y=t*tile_y
            self.canvas.create_line(0,y,width,y,tags="grid")
            self.canvas.create_line(width/2-5,y,width/2+5,y,width=4,tags="grid")

    def update(self, model):
        self.plot_signal(model.get_signal(),model.get_name())
        print("update")
        
    def packing(self) :
        self.canvas.pack(expand=1,fill="both",padx=6)
        
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Osciloscope")
    
    screen = Screen(root)
    screen.set_tiles(10)
    screen.create_grid()
    
    gen = Generator()
    gen.attach(screen)
    gen.generate()
    
    screen.plot_signal(gen.get_signal(),gen.get_name())
    screen.packing()
    root.mainloop()
    