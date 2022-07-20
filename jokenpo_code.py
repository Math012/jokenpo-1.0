#This program was developed by me, and its mission is help me to study the Python language, sorry for
# any problems in this code or errors related to logic 
from tkinter import *
from random import *
from PIL import Image, ImageTk
root = Tk()

# Create my class that will contain the principal "def"
class ProgramMain():
    def __init__(self):
        self.root = root
        self.Window()
        self.Frames()
        self.ElementsFrames()
        root.mainloop()

# Create elements for Window 
    def Window(self):
        self.root.title("Jokenpo")
        self.root.configure(background='#f1f1f1')
        self.root.geometry("400x500")
        self.root.minsize(width=400, height=500)
        self.root.maxsize(width=400, height=500)
    
# Created a Frame for help me related the orietation the buttons     
    def Frames(self):
        self.frame = Frame(self.root, bg='#f1f1f1', bd=4)
        self.frame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.44)
   

    def ElementsFrames(self):
        #import images necessary with library PIL
        # "empate = draw", "perdeu = lose", "ganhou = win", "padrão = default", "papel = paper", "pedra = stone", "tesoura = scissors"
        self.draw_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/empate.png'))
        self.lose_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/perdeu.png'))
        self.win_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/ganhou.png'))
        self.default_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/padrao.png'))
        self.paper_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/papel.png'))
        self.stone_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/pedra.png'))
        self.scissors_img = ImageTk.PhotoImage(Image.open('c:\jokenpo/tesoura.png'))
        #CREATE BUTTONS 
        # 1 = PAPER BUTTONN
        self.bt_paper = Button(self.frame, image=self.paper_img, borderwidth=0, command=self.Paper)
        self.bt_paper.place(relx=0.0, rely=0.3, relwidth=0.3, relheight=0.5)
        # 2 = STONE BUTTON
        self.bt_stone = Button(self.frame, image=self.stone_img, borderwidth=0, command=self.Stone)
        self.bt_stone.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.5)
        # 3 = SCISSORS BUTTON
        self.bt_scissors = Button(self.frame, image=self.scissors_img, borderwidth=0, command=self.Scissor)
        self.bt_scissors.place(relx=0.7, rely=0.3, relwidth=0.3, relheight=0.5)

        # CREATE A LABEL DEFAULT
        self.bt_label = Label(image=self.default_img)
        self.bt_label.place(relx=0.38, rely=0.1)

    def ChoisePc(self):
        n1 = randint(1, 3)
        return n1            
            
    def Paper(self):
        n2 = 1
        self.ChoisePc()
        if self.ChoisePc() == 1 and n2 == 1:
            self.label_paper = Label(image=self.paper_img)
            self.label_paper.place(relx=0.38, rely=0.1)
            self.labeldraw = Label(image=self.draw_img)
            self.labeldraw.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 2 and n2 == 1:
            self.label_stone = Label(image=self.stone_img)
            self.label_stone.place(relx=0.38, rely=0.1)
            self.labelwin = Label(image=self.win_img)
            self.labelwin.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 3 and n2 == 1:
            self.label_scissors = Label(image=self.scissors_img)
            self.label_scissors.place(relx=0.38, rely=0.1)
            self.labellose = Label(image=self.lose_img)
            self.labellose.place(relx=0.35, rely=0.4)          

    def Stone(self):
        n3 = 2
        self.ChoisePc()
        if self.ChoisePc() == 2 and n3 == 2:
            self.label_stone = Label(image=self.stone_img)
            self.label_stone.place(relx=0.38, rely=0.1)
            self.labeldraw = Label(image=self.draw_img)
            self.labeldraw.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 3 and n3 == 2:
            self.label_scissors = Label(image=self.scissors_img)
            self.label_scissors.place(relx=0.38, rely=0.1)
            self.labelwin = Label(image=self.win_img)
            self.labelwin.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 1 and n3 == 2:
            self.label_paper = Label(image=self.paper_img)
            self.label_paper.place(relx=0.38, rely=0.1)
            self.labellose = Label(image=self.lose_img)
            self.labellose.place(relx=0.35, rely=0.4)     

    def Scissor(self):
        n4 = 3
        if self.ChoisePc() == 3 and n4 == 3:
            self.label_scissors = Label(image=self.scissors_img)
            self.label_scissors.place(relx=0.38, rely=0.1)
            self.labeldraw = Label(image=self.draw_img)
            self.labeldraw.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 1 and n4 == 3:
            self.label_paper = Label(image=self.paper_img)
            self.label_paper.place(relx=0.38, rely=0.1)
            self.labelwin = Label(image=self.win_img)
            self.labelwin.place(relx=0.35, rely=0.4)

        elif self.ChoisePc() == 2 and n4 == 3:
            self.label_stone = Label(image=self.stone_img)
            self.label_stone.place(relx=0.38, rely=0.1)
            self.labellose = Label(image=self.lose_img)
            self.labellose.place(relx=0.35, rely=0.4)          
ProgramMain()
               