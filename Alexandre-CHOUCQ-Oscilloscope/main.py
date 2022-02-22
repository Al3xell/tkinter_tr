# -*- coding: utf-8 -*-
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from math import pi,sin
from utils import radians
# import logging
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(level=logging.CRITICAL)
# logger = logging.getLogger(__name__)

class Simulator :
    def __init__(self,parent,bg="white",name="signal",mag=0.5,freq=2.0,phase=0.0,harmonics=1):
        self.parent=parent
        self.name=name
        self.mag,self.freq,self.phase,self.harmonics=mag,freq,phase,harmonics
        self.signal=[]
        self.harmo_odd_even=1
        self.samples=100
        self.canvas=tk.Canvas(parent,bg=bg)
        self.canvas.bind("<Configure>", self.resize)
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))
        self.resize=False
        self.tiles=4
        self.create_controls()
    def __repr__(self):
        return "<Screen(mag:{}, freq:{}, phase:{}, harmonics :{})>".format(self.mag,self.freq,self.phase,self.harmonics)
    def get_signal(self):
        # signal=copy.copy(self.signal)
        return self.signal
    def get_canvas(self) :
        return self.canvas

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_magnitude(self):
        return self.mag
    def set_magnitude(self,mag):
        self.mag=mag
    def get_frequency(self):
        return self.freq
    def set_frequency(self,freq):
        self.freq=freq
    def get_phase(self):
        return self.phase
    def set_phase(self,phase):
        self.phase=phase
    def get_harmonics(self) :
        return self.harmonics    
    def set_harmonics(self,harmonics=1) :
        self.harmonics=harmonics
    def get_samples(self):
        return self.samples
    def set_samples(self,samples):
        self.samples=samples
    def get_tiles(self):
        return self.tiles
    def set_tiles(self,tiles):
        self.tiles=tiles

    def vibration(self,t):
        a,f,p,harmonics=self.mag,self.freq,self.phase,self.harmonics
        p_to_r=radians(p)
        sum=a*sin(2*pi*f*t)-p_to_r
        for h in range(2,harmonics+1) :
            if  self.harmo_odd_even==1  :
                sum=sum+(a*1.0/h)*sin(2*pi*(f*h)*t-p_to_r)
            elif  self.harmo_odd_even==2 and h%2==1 :
                sum=sum+(a*1.0/h)*sin(2*pi*(f*h)*t-p_to_r)
        return sum
    def generate(self,period=2):
        del self.signal[0:]
        echantillons=range(int(self.samples)+1)
        Tech=period/self.samples
        for t in echantillons :
            self.signal.append([t*Tech,self.vibration(t*Tech)])
        return self.signal
    def delete(self):
        del self.signal[0:]
        self.notify()
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

    def create_controls(self):
        self.mag_var=tk.DoubleVar()
        self.mag_var.set(self.get_magnitude())
        self.scale_mag=tk.Scale(self.parent,variable=self.mag_var,
                          label="Amplitude",
                          orient="horizontal",length=250,
                          from_=0,to=1,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=0.5,
                          command=self.cb_update_magnitude)
        self.harmonics_var=tk.IntVar()
        self.harmonics_var.set(self.get_harmonics())
        self.scale_harmonics=tk.Scale(self.parent,variable=self.harmonics_var,
                          label="Harmonics",
                          orient="horizontal",length=250,
                          from_=1,to=50,relief="raised",
                          sliderlength=20,tickinterval=5,
                          command=self.cb_update_harmonics)
        frame=tk.LabelFrame(self.parent,text="Harmonics")
        self.radio_var=tk.IntVar()
        btn=tk.Radiobutton(frame,text="All", variable=self.radio_var,value=1,command=self.cb_activate_button)
        btn.select()
        btn.pack(anchor ="w")
        btn=tk.Radiobutton(frame,text="Odd", variable=self.radio_var,value=2,command=self.cb_activate_button)
        btn.pack(anchor ="w")
        frame.pack()

    def cb_update_magnitude(self,event):
        print("cb_update_magnitude(self,event)",self.mag_var.get())
        self.set_magnitude(self.mag_var.get())
        self.generate()
        self.plot_signal(self.signal,self.name)

    def cb_update_harmonics(self,event):
        print("cb_update_harmonics(self,event)",self.harmonics_var.get())
        self.set_harmonics(self.harmonics_var.get())
        self.generate()
        self.plot_signal(self.signal,self.name)

    def cb_activate_button(self):
        print("You selected the option " + str(self.radio_var.get()))
        self.harmo_odd_even=self.radio_var.get()

    def resize(self, event):
        self.width = event.width
        self.height = event.height
        print("resize : ",self.width,self.height)
        self.canvas.delete("grid")
        self.create_grid()
        self.plot_signal(self.signal,self.name)

    def packing(self) :
        self.canvas.pack(expand=1,fill="both",padx=6)
        self.scale_mag.pack()
        self.scale_harmonics.pack()

if   __name__ == "__main__" :
    root=tk.Tk()
    root.title("Dupond/Dupont : X-Y Simulator")
    simulator=Simulator(root)
    simulator.generate()
    simulator.set_tiles(tiles=10)
    simulator.create_grid()
    simulator.plot_signal(simulator.get_signal(),simulator.get_name())
    simulator.packing()
    root.mainloop()

