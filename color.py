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

        self.iRouge = 0
        self.iBleu = 0
        
        self.iWhite = 0
        self.iBlack = 0

        self.entryNb = 0

        self.range = 5
        
        self.flagExp2 = False
        self.flagExp3 = False

        # self.firstPage()
        name = sys.stdin
        self.f = sys.stdout
        self.teintTest()
        self.window.mainloop()
        self.f.close()

    def toggleFullScreen(self , event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self , event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def nextColorTeint(self , event):
        self.clearWin()
        if(255 -self.range*self.iRouge>0):
            self.iRouge += 1
            self.bg = self._from_rgb(255 -self.range*self.iRouge, 255, 0)
        else:
            self.iBleu += 1
            self.bg=self._from_rgb(0, 255,self.range*self.iBleu)
        self.window.configure(bg=self.bg) 
        self.writeWord()

        if(self.bg == self._from_rgb(0,255,255) or self.entryNb == 2):
            self.clearWin()
            self.flagExp2 = True
            self.window.bind("<space>",self.nextColorL)
        
    def nextColorL(self , event):
        self.clearWin()
        if(255 -self.range*self.iWhite>0 and self.entryNb == 2):
            self.iWhite += 1
            self.bg = self._from_rgb(255 -self.range*self.iWhite, 255, 255 -self.range*self.iWhite)
        else:
            self.flagExp3 = True
            self.window.bind("<space>",self.nextColorS)
        
        self.window.configure(bg=self.bg) 
        self.writeWord()

    def nextColorS(self , event):
        self.clearWin()
        if(255 -self.range*self.iBlack>0):
            self.iBlack += 1
            self.bg=self._from_rgb(0, 255-self.range*self.iBlack,0)
        self.window.configure(bg=self.bg) 
        self.writeWord()
        
    def writeWord(self):    
        self.greenWord = tk.Label(self.window, text=wordList[np.random.randint(len(wordList))], bg = self.bg, fg = self._from_rgb(0,255,0))
        self.greenWord.place(relx = np.random.randint(10,91)/100 , rely = np.random.randint(10,91)/100 , anchor = 'center')


    def _from_rgb(self,r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def clearWin(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def teintTest(self):
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.bind("<space>", self.nextColorTeint)
        self.window.bind("<Return>", self.writeData)
        
        self.bg=self._from_rgb(255, 255, 0)
        self.writeWord()
        self.window.configure(bg = self.bg)

    def lsTest(self):
        self.window.bind("<space>", self.nextColorL)
        self.window.bind("<Return>", self.writeData)
        
        self.bg=self._from_rgb(255, 255, 255)
        self.writeWord()
        self.window.configure(bg = self.bg)


    # def createNewFileAndCleanWin(self,name):
    #     name = self.name_Tf.get()
    #     fileName = name + ".txt"
    #     self.clearWin()
    #     self.f = open(fileName,'a')
    #     self.teintTest()
    
    def writeData(self , event):
        self.entryNb += 1
        if(self.entryNb == 1):
            self.f.write("Premier seuil teint : ")
            self.f.write(str(255 -self.range*self.iRouge) +",255,"+ str(self.range*self.iBleu)+"\n")
        elif(self.entryNb == 2):
            self.f.write("Second seuil teint : ")
            self.f.write(str(255 -self.range*self.iRouge) +",255,"+ str(self.range*self.iBleu)+"\n")
        elif(self.entryNb == 3 and self.flagExp2):
            self.f.write("Seuil luminausité : ")
            self.f.write(str(255 -self.range*self.iWhite) +",255,"+ str(255 -self.range*self.iWhite)+"\n") 
        elif(self.entryNb == 4 and self.flagExp3):
            self.f.write("Seuil saturation :")
            self.f.write("0,"+str(255-self.range*self.iBlack)+",0\n")
            self.window.destroy()

ColorWin()
