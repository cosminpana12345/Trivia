from tkinter import *
from tkinter import ttk
from random import seed
from random import randint

class Question:
    mq = None
    mRightAnswer = None
    mWrongNaswer1 = None
    mWrongAnswer2 = None
    def __init__(self, q, rightAnswer, wrongAnswer1, wrongAnswer2):
        self.mq = q
        self.mRigthAnswer = rightAnswer
        self.mWrongAnswer1 = wrongAnswer1
        self.mWrongAnswer2 = wrongAnswer2

    def printq(self):
        print(self.mq, " are raspunsul ", self.mRightAnswer, " iar ", self.mWrongAnswer1, " si ", self.mWrongAnswer2, " sunt gresite")

q1 = [Question('Intrebarea 1', 'Raspunsul corect 1', 'Raspunsul gresit 1_1', 'Raspunsul gresit 1_2'),
      Question('Intrebarea 2', 'Raspunsul corect 2', 'Raspunsul gresit 2_1', 'Raspunsul gresit 2_2'),
      Question('Intrebarea 3', 'Raspunsul corect 3', 'Raspunsul gresit 3_1', 'Raspunsul gresit 3_2'),
      Question('Intrebarea 4', 'Raspunsul corect 4', 'Raspunsul gresit 4_1', 'Raspunsul gresit 4_2'),
      Question('Intrebarea 5', 'Raspunsul corect 5', 'Raspunsul gresit 5_1', 'Raspunsul gresit 5_2'),
      Question('Intrebarea 6', 'Raspunsul corect 6', 'Raspunsul gresit 6_1', 'Raspunsul gresit 6_2'),
      Question('Intrebarea 7', 'Raspunsul corect 7', 'Raspunsul gresit 7_1', 'Raspunsul gresit 7_2'),
      Question('Intrebarea 8', 'Raspunsul corect 8', 'Raspunsul gresit 8_1', 'Raspunsul gresit 8_2'),
      Question('Intrebarea 9', 'Raspunsul corect 9', 'Raspunsul gresit 9_1', 'Raspunsul gresit 9_2'),
      # Question('Intrebarea 11', 'Raspunsul corect 11', 'Raspunsul gresit 11_1', 'Raspunsul gresit 11_2'),
      # Question('Intrebarea 12', 'Raspunsul corect 12', 'Raspunsul gresit 12_1', 'Raspunsul gresit 12_2'),
      # Question('Intrebarea 13', 'Raspunsul corect 13', 'Raspunsul gresit 13_1', 'Raspunsul gresit 13_2'),
      # Question('Intrebarea 14', 'Raspunsul corect 14', 'Raspunsul gresit 14_1', 'Raspunsul gresit 14_2'),
      # Question('Intrebarea 15', 'Raspunsul corect 15', 'Raspunsul gresit 15_1', 'Raspunsul gresit 15_2'),
      # Question('Intrebarea 16', 'Raspunsul corect 16', 'Raspunsul gresit 16_1', 'Raspunsul gresit 16_2'),
      # Question('Intrebarea 17', 'Raspunsul corect 17', 'Raspunsul gresit 17_1', 'Raspunsul gresit 17_2'),
      # Question('Intrebarea 18', 'Raspunsul corect 18', 'Raspunsul gresit 18_1', 'Raspunsul gresit 18_2'),
      # Question('Intrebarea 19', 'Raspunsul corect 19', 'Raspunsul gresit 19_1', 'Raspunsul gresit 19_2'),
      # Question('Intrebarea 20', 'Raspunsul corect 20', 'Raspunsul gresit 20_1', 'Raspunsul gresit 20_2'),
      ]

# for j in range(6):
#     n = randint(0, len(copy_q1)-1)
#     random_numbers.insert(len(random_numbers), n)
#     copy_q1[n].printq()
#     del copy_q1[n]

class Application(Frame):
    def __init__(self, master=None, Frame=None):
        Frame.__init__(self, master)
        super(Application,self).__init__()
        self.grid(column = 0, row = 1, padx=200, pady=170)
        self.createMenuWidgets()

    def startgame(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=1, padx=25, pady=125)
        self.createGameWidgets()

    def info(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=1, padx=200, pady=150)
        self.createInfoWidgets()

    def callBack(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=1, padx=200, pady=150)
        self.createMenuWidgets()

    def createEndWidgets(self):
        self.destroy()
        super(Application, self).__init__()
        self.grid(column=0, row=1, padx=200, pady=150)
        Label(self, text='Scor: ' + str(self.score) +'/5').grid(row=0)
        Button(self, text='Menu', command=self.callBack).grid(row=1)

    def checkAnswer(self):
        self.total = self.total+1
        if self.v.get() == self.raspunsCorect:
            self.score = self.score+1
        # self.nextButton.config(state='normal')

    def callNextButton(self):
        if self.total < 5:
            self.destroy()
            super(Application, self).__init__()
            self.grid(column=0, row=1, padx=25, pady=125)
            self.createGameWidgets()
        else:
            self.createEndWidgets()

    def createGameWidgets(self):
        self.raspunsuri = []
        self.raspunsuriRandom = []
        self.radio_btns = []

        n = randint(0, len(self.copy_q1) - 1)
        n_in_rand = 1
        while n_in_rand == 1:
            if n in self.random_numbers:
                n = n = randint(0, len(self.copy_q1) - 1)
            else:
                n_in_rand = 0
        self.random_numbers.insert(len(self.random_numbers), n)

        self.intrebare = self.copy_q1[n].mq
        self.raspunsuri = [self.copy_q1[n].mRigthAnswer, self.copy_q1[n].mWrongAnswer1, self.copy_q1[n].mWrongAnswer2]
        self.copyRaspunsuri = self.raspunsuri
        self.raspunsCorect = self.copy_q1[n].mRigthAnswer

        #intrebarea
        self.questionLabel = Label(self, text=self.intrebare, borderwidth=1, relief="groove").grid(row=0, column=0, columnspan=3, ipadx=50, ipady=25, pady=15)

        # butoane
        self.backButton = ttk.Button(self, text='Back to menu', command=self.callBack).grid(row=2, column=0, pady=25, padx=25)
        self.nextButton = ttk.Button(self, text='Next question', state='normal', command=self.callNextButton).grid(row=2, column=1, pady=25, padx=25)
        self.scoreWidget = Label(self, text=str(self.score)+'/'+str(self.total)).grid(row=2, column=2, padx=25)

        #raspunsuri
        self.v = StringVar()
        self.v.set('None')
        Radiobutton(self, width=20, variable=self.v, anchor=W, text='None', value='None')

        self.raspunsuriRandom = []
        m = randint(0, len(self.raspunsuri) - 1)
        self.raspunsuriRandom.append(self.raspunsuri[m])
        del self.raspunsuri[m]
        m = randint(0, len(self.raspunsuri) - 1)
        self.raspunsuriRandom.append(self.raspunsuri[m])
        del self.raspunsuri[m]
        self.raspunsuriRandom.append(self.raspunsuri[0])

        for i in range(3):
            self.radio_btns.append(Radiobutton(self, text=self.raspunsuriRandom[i], variable=self.v, value=self.raspunsuriRandom[i], command=self.checkAnswer))
            self.radio_btns[i].deselect()
            self.radio_btns[i].grid(row=1, column=i, pady=25, padx=25)

        # del self.copy_q1[n]

    def createInfoWidgets(self):
        self.infoLabel = Label(self, text='Regulile jocului').grid(row=0, pady=25)
        self.backButton2 = Button(self, text='Back', command=self.callBack).grid(row=1)

    def createMenuWidgets(self):
        self.score = 0
        self.total = 0
        self.copy_q1 = q1
        self.random_numbers = []

        #impartirea in pagina
        self.topframe = Frame(self)
        self.topframe.grid(row=0, column=0)

        self.bottomframe = Frame(self)
        self.bottomframe.grid(row=1, column=0)

        #butoane
        self.startButton = Button(self.topframe, text='Start', height=2, width=10, command=self.startgame)
        self.startButton.pack(side=BOTTOM, pady=20)
        self.infoButton = Button(self.bottomframe, text='Info', height=2, width=10, command=self.info)
        self.infoButton.pack(side=TOP)


app = Application()
app.master.title('Trivia')
app.master.resizable(False, False)
app.mainloop()
