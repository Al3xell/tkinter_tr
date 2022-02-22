from observer import Subject
from utils import radians


from math import pi,sin
#import copy

class Generator(Subject):
 
#-----Constructor-----#
    def __init__(self, name="signal",mag=0.5,freq=2.0,phase=0.0,harmonics=1):
        super().__init__()
        self.name=name
        self.mag=mag
        self.freq=freq
        self.phase=phase
        self.harmonics=harmonics
        self.samples=100
        self.signal=[]
        self.harmo_odd_even=1

#-----___str___-----#

    def __repr__(self):
        return "Generator()"

    def __str__(self):
        return f'\nGenerator : name = {self.name}, frequency = {self.freq}, phase = {self.phase}, harmonics = {self.harmonics}, samples = {self.samples}\n'

#-----Getter-----#
    def get_name(self):
        return self.name
    def get_magnitude(self):
        return self.mag
    def get_freq(self):
        return self.freq
    def get_phase(self):
        return self.phase
    def get_harmonics(self) :
        return self.harmonics
    def get_samples(self):
        return self.samples
    def get_signal(self):
        # signal=copy.copy(self.signal)
        return self.signal
#-----Setter-----#
    def set_name(self,name):
        self.name=name
    def set_magnitude(self,mag):
        self.mag=mag
    def set_freq(self,freq):
        self.freq=freq
    def set_phase(self,phase):
        self.phase=phase
    def set_harmonics(self,harmonics=1) :
        self.harmonics=harmonics
    def set_samples(self,samples):
        self.samples=samples
        
#-----Methods-----#

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
        self.notify()
        return self.signal
    
    def delete(self):
        del self.signal[0:]
        # self.notify()

    
if __name__ == "__main__":
    gen = Generator()
    print(gen)
    gen.generate()
    print(gen.get_signal())