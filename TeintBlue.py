import sys
import tkinter as tk
import numpy as np 

wordList = ["maison","tête","ville","temps","porte" ,"pays","route","raison",
"homme","cœur","femme","dieu","amour","monde" ,"voiture" ,"jour",
"temps","monsieur","bien","personne","fois" ,"part" ,"rue" ,"chambre","monde"]

class TeintBlue():

    #Tous les compteurs
    iBlue = 0

    #Variable constante
    range = 5
    f = sys.stdout #fichier où on écrit les résultats de l'expérience

    #Flag pour passer d'une expérience à une autre

    #Création de l'interface
    window = tk.Tk()
    
    window.title("Color Experiment")
    fullScreenState = False
    window.attributes("-zoomed", True)
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d" % (w, h))

    def __init__(self,filename) -> None:
        self.f = open(filename,'a+')

    #Fonction de base pour l'interface
    def toggleFullScreen(self , event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self , event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def defineBaseHotkey(self):
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

    #Fonction écrivant un mot dans la fentre de couleur verte et en position aléatoire
    def writeWord(self):    
        self.greenWord = tk.Label(self.window, text=wordList[np.random.randint(len(wordList))], bg = self.bg, fg = self._from_rgb(0,255,0))
        self.greenWord.place(relx = np.random.randint(10,91)/100 , rely = np.random.randint(10,91)/100 , anchor = 'center')

    #Fonction traduisant du rgb en html
    def _from_rgb(self,r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'

    #Fonction enlevant tous les éléments présents dans l'interface (les mots, bouttons etc)
    def clearWin(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def showWord(self):
        self.greenWord.configure(fg = self._from_rgb(0,0,0))

    def quitWin(self , event):
        self.window.destroy()

    ##Expérience 2 : teint en allant vers le bleu
    def firstPageTeintBlue(self):
        self.window.configure(bg =self._from_rgb(255, 255, 255))
        str = tk.Label(self.window, text="Press any <Space> to start" , fg = "black" , bg ="white")
        str.place(relx = 0.5 , rely = 0.5 , anchor = 'center')
        self.window.bind("<space>",self.teintTestBlue)
        self.window.mainloop()

    def teintTestBlue(self, event):
        """Fonction réalisant le test de teint"""
        self.clearWin()
        self.window.bind("<space>", self.nextColorTB)
        self.window.bind("<Return>", self.writeDataTB)
        
        self.bg=self._from_rgb(0, 255, 255)
        self.writeWord()
        self.window.configure(bg = self.bg)
        self.window.mainloop()

    def nextColorTB(self , event = None):
        """Fonction permettant de passer à la prochaine couleur dans l'expérience 1 """
        self.showWord()
        self.window.bind("<space>", self.configBgExp2)
        self.window.bind("<Return>", self.writeDataTB)
    
    def configBgExp2(self , event):
        """Fonction permettant de changer à la prochaine couleur dans l'expérience 1"""
        self.window.bind("<space>", self.nextColorTB)
        self.clearWin()
        if(255 -self.range*self.iBlue>0):
            self.iBlue += 1
            self.bg = self._from_rgb(0,255,255-self.range*self.iBlue)
        else:
            event = None
            self.window.destroy()
        self.window.configure(bg=self.bg) 
        self.writeWord()
    
    def writeDataTB(self , event):
        self.window.unbind("<Return>")
        self.window.unbind("<space>")
        self.window.bind("<Return>",self.quitWin)
        self.f.write("Seuil bleu teint : "+ "0,255," +str(255-self.range*self.iBlue)+"\n")
        self.str = tk.Label(self.window, text="Data Writen , please press <Enter>" , fg = "black" , bg = "white")
        self.str.place(relx = 0.5 , rely = 0.5 , anchor = 'center')

interface  = TeintBlue("test.txt")
interface.firstPageTeintBlue()
