from generator import *
from screen import *
    
class Controller(object):

#-----Constructor-----#
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.get_canvas().bind("<Configure>", self.resize)
 
#-----Getter-----#
    def get_model(self):
        return self.model
    
    def get_view(self):
        return self.view
 
#-----Setter-----#
    def set_model(self, model):
        self.model = model
    def set_view(self, view):
        self.view = view
        
#-----Methods----#
    def create_controls(self):
        frame_scale = tk.LabelFrame(self.view.get_parent(),text="Scales")
        self.mag_var=tk.DoubleVar()
        self.mag_var.set(self.model.get_magnitude())
        self.scale_mag=tk.Scale(frame_scale,
                                variable=self.mag_var,
                                label="Amplitude",
                                orient="horizontal",length=self.view.get_width(),
                                from_=0,to=1,relief="raised",
                                sliderlength=20,resolution = 0.1,
                                tickinterval=0.5,
                                command=self.cb_update_magnitude)
        self.harmonics_var=tk.IntVar()
        self.harmonics_var.set(self.model.get_harmonics())
        self.scale_harmonics=tk.Scale(frame_scale,
                                      variable=self.harmonics_var,
                                      label="Harmonics",
                                      orient="horizontal",length=self.view.get_width(),
                                      from_=1,to=50,relief="raised",
                                      sliderlength=20,tickinterval=5,
                                      command=self.cb_update_harmonics)
        self.freq_var=tk.IntVar()
        self.freq_var.set(self.model.get_freq())
        self.scale_freq=tk.Scale(frame_scale,
                                      variable=self.freq_var,
                                      label="Freq",
                                      orient="horizontal",length=self.view.get_width(),
                                      from_=0,to=5000,relief="raised",
                                      sliderlength=20,tickinterval=1000,
                                      command=self.cb_update_freq)
        self.phase_var=tk.DoubleVar()
        self.phase_var.set(self.model.get_phase())
        self.scale_phase=tk.Scale(frame_scale,
                                      variable=self.phase_var,
                                      label="phase",
                                      orient="horizontal",length=self.view.get_width(),
                                      from_=-1,to=1,relief="raised",
                                      sliderlength=20, resolution = 0.1,
                                      tickinterval=0.5,
                                      command=self.cb_update_phase)
        frame_scale.pack(fill="x", expand=1)
        frame=tk.LabelFrame(self.view.get_parent(),text="Harmonics")
        self.radio_var=tk.IntVar()
        btn=tk.Radiobutton(frame,text="All", variable=self.radio_var,value=1,command=self.cb_activate_button)
        btn.select()
        btn.pack(anchor ="w")
        btn=tk.Radiobutton(frame,text="Odd", variable=self.radio_var,value=2,command=self.cb_activate_button)
        btn.pack(anchor ="w")
        frame.pack()

    def cb_update_magnitude(self,event):
        print("cb_update_magnitude(self,event)",self.mag_var.get())
        self.model.set_magnitude(self.mag_var.get())
        self.model.generate()
        self.view.plot_signal(self.model.get_signal(),self.model.get_name())

    def cb_update_harmonics(self,event):
        print("cb_update_harmonics(self,event)",self.harmonics_var.get())
        self.model.set_harmonics(self.harmonics_var.get())
        self.model.generate()
        self.view.plot_signal(self.model.get_sigHarmonicsnal(),self.model.get_name())
        
    def cb_update_freq(self,event):
        print("cb_update_freq(self,event)",self.freq_var.get())
        self.model.set_freq(self.freq_var.get())
        self.model.generate()
        self.view.plot_signal(self.model.get_signal(),self.model.get_name())
        
    def cb_update_phase(self,event):
        print("cb_update_freq(self,event)",self.phase_var.get())
        self.model.set_phase(self.phase_var.get())
        self.model.generate()
        self.view.plot_signal(self.model.get_signal(),self.model.get_name())

    def cb_activate_button(self):
        print("You selected the option " + str(self.radio_var.get()))
        self.model.harmo_odd_even=self.radio_var.get()
        
    def resize(self, event):
        self.view.width = event.width
        self.view.height = event.height
        print("resize : ",self.view.width,self.view.height)
        self.view.get_canvas().delete("grid")
        self.view.create_grid()
        self.model.notify()
        
    def packing(self) :
        self.scale_mag.pack(fill="x", expand=0.8)
        self.scale_harmonics.pack(fill="x", expand=0.8)
        self.scale_freq.pack(fill="x", expand=0.8)
        self.scale_phase.pack(fill="x", expand=0.8)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("test")
    
    screen = Screen(root)
    screen.set_tiles(10)
    screen.create_grid()
    
    gen = Generator()
    gen.attach(screen)
    gen.generate()
    
    screen.plot_signal(gen.get_signal(),gen.get_name())
    screen.packing()
    
    ctrl = Controller(gen, screen)
    ctrl.create_controls()
    ctrl.packing()

    root.mainloop()
    