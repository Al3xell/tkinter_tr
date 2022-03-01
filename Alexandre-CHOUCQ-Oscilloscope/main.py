# -*- coding: utf-8
from controller import *
from menubar import MenuBar

if   __name__ == "__main__" :
    root = tk.Tk()
    root.title("Oscilloscope")

    
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
    
        
    menu = MenuBar(ctrl)

    root.mainloop()

