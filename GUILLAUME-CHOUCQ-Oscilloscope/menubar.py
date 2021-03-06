import json

from controller import *
from PIL import ImageGrab

    
class MenuBar(object):
    """
    docstring for MenuBar.
    """
    
    def __init__(self, controller):
        
                
        self.controller = controller
        
        self.menubar = tk.Menu(self.controller.get_view().get_parent())

        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="Open", command=self.onOpen)
        self.filemenu.add_command(label="Save As", command=self.onSave)
        self.filemenu.add_command(label="Save Image", command=self.onSaveImg)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.onExit)

        self.helpmenu = tk.Menu(self.menubar, tearoff=False)
        self.helpmenu.add_command(label="About Us")
        self.helpmenu.add_command(label="About TK")
        self.helpmenu.add_command(label="About Python")
        
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        

        self.controller.get_view().get_parent().config(menu=self.menubar)
            
    def onOpen(self):
        
        filename = filedialog.askopenfilename(initialdir = "$HOME",title = "Open file",filetypes = (("Json Parameters","*.json"),("All files","*.*")))
        
        f = open(filename, "r")
        data = json.load(f)
        
        self.controller.model = Generator(data['name'],data['mag'],data['freq'],data['phase'],data['harmonics'],data['samples'],data['signal'],data['harmo_odd_even'])
        self.controller.model.attach(self.controller.view)
        self.controller.model.notify()
        f.close()
    
    def onSave(self):
        
        filename = filedialog.asksaveasfile(initialdir = "$HOME",initialfile = 'Signal.json',title = "Save as",filetypes = [('JSON File', '*.json')], defaultextension=json)
        data = self.data()
        json.dump(data, filename)
        
    def onSaveImg(self):
        x = tk.Canvas.winfo_rootx(self.controller.view.canvas)
        y = tk.Canvas.winfo_rooty(self.controller.view.canvas)
        w = tk.Canvas.winfo_width(self.controller.view.canvas)
        h = tk.Canvas.winfo_height(self.controller.view.canvas)
        MsgBox =  tk.messagebox.showinfo(title='Sauvegarder !', message='Signal sauvergarder !')
        img= ImageGrab.grab((x, y, x+w, y+h)).save('Canva.png')
 
    
    def onExit(self):
        MsgBox = tk.messagebox.askquestion ('Voulez vous quitter ?','Etes vous s??r ?',icon = 'error')
        if MsgBox == 'yes':
            self.controller.view.parent.destroy()
            
    
    def data(self):
        data = {}
        
        data['name'] = self.controller.model.name
        data['mag'] = self.controller.model.mag
        data['freq'] = self.controller.model.freq
        data['phase'] = self.controller.model.phase
        data['harmonics'] = self.controller.model.harmonics
        data['samples'] = self.controller.model.samples
        data['signal'] = self.controller.model.signal
        data['harmo_odd_even'] = self.controller.model.harmo_odd_even
        
        return data
