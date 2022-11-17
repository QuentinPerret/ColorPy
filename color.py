import sys
import tkinter as tk
import matplotlib.colors as col #for hsv to rgb

class ColorWin():
    
    def __init__(self) -> None:
            
        self.window = tk.Tk()
        self.window.title("Color Experiment")
        self.fullScreenState = False
        self.window.attributes("-zoomed", True)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))

        self.iTeintRouge = 0
        self.iTeintBleu = 0
        self.range = 5

        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.bind("<space>", self.nextColor)

        self.window.configure(bg=self._from_rgb(255, 255, 0)) 

        self.window.mainloop()

    def toggleFullScreen(self , event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self , event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def nextColor(self , event):
        if(255 -self.range*self.iTeintRouge>0):
            self.iTeintRouge += 1
            self.window.configure(bg=self._from_rgb(255 -self.range*self.iTeintRouge, 255, 0)) 
        else:
            self.iTeintBleu += 1
            self.window.configure(bg=self._from_rgb(0, 255,self.range*self.iTeintBleu)) 
        print(self.range*self.iTeintRouge,self.range*self.iTeintBleu )

    def _from_rgb(self,r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'

ColorWin()
