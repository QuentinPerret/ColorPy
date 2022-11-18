import sys
import tkinter as tk
import matplotlib.colors as col #for hsv to rgb
import numpy as np 

wordList = ["maison","tête","ville","temps","porte" ,"pays","route","raison",
"homme","cœur","femme","dieu","amour","monde" ,"voiture" ,"jour",
"temps","monsieur","bien","personne","fois" ,"part","rue" ,"chambre","monde"]

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

        self.firstPage()

        self.window.mainloop()
        self.f.close()

    def toggleFullScreen(self , event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self , event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def nextColor(self , event):
        self.clearWin()
        if(255 -self.range*self.iTeintRouge>0):
            self.iTeintRouge += 1
            self.bg = self._from_rgb(255 -self.range*self.iTeintRouge, 255, 0)
        else:
            self.iTeintBleu += 1
            self.bg=self._from_rgb(0, 255,self.range*self.iTeintBleu)
        
        self.window.configure(bg=self.bg) 
        self.greenWord = tk.Label(self.window, text=wordList[np.random.randint(len(wordList))], bg = self.bg, fg = self._from_rgb(0,255,0))
        self.greenWord.place(relx = np.random.randint(10,91)/100 , rely = np.random.randint(10,91)/100 , anchor = 'center')


    def _from_rgb(self,r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def firstPage(self):
        tk.Label(self.window, text='Enter The Subject Name & Hit Enter Key').pack(pady=20)
        self.name_Tf = tk.Entry(self.window)
        self.name_Tf.bind('<Return>',self.createNewFileAndCleanWin)
        self.name_Tf.pack()

    def clearWin(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def teintTest(self):
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.bind("<space>", self.nextColor)
        self.window.bind("<Return>", self.writeData)

        self.window.configure(bg=self._from_rgb(255, 255, 0))

    def createNewFileAndCleanWin(self,name):
        name = self.name_Tf.get()
        fileName = name + ".txt"
        self.clearWin()
        self.f = open(fileName,'a')
        self.teintTest()
    
    def writeData(self , event):
        print(str(255 -self.range*self.iTeintRouge) +",255,"+ str(self.range*self.iTeintBleu))
        self.f.write(str(255 -self.range*self.iTeintRouge) +",255,"+ str(self.range*self.iTeintBleu)+"\n")


ColorWin()
