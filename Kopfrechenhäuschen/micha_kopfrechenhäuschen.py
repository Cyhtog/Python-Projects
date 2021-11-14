from tkinter import *
import random

class PyramidenRechnen():
    def __init__(self):
        self.master = Tk()
        random.seed()
        self.master.title("Das Kopfrechenhäuschen")
        self.master.config(bg="light green")
        self.master.resizable(width=False, height=False)
        self.alterWert = ""
        self.gewaehltesFeld = 21
        self.y = 10

        self.var11 = random.randint(1, self.y)
        self.var12 = random.randint(1, self.y)
        self.var13 = random.randint(1, self.y)
        self.var14 = random.randint(1, self.y)
        self.var15 = random.randint(1, self.y)

        self.lbl11 = Label(self.master, text=self.var11, font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl12 = Label(self.master, text=self.var12, font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl13 = Label(self.master, text=self.var13, font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl14 = Label(self.master, text=self.var14, font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl15 = Label(self.master, text=self.var15, font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl21 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl22 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl23 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl24 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl31 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl32 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl33 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl41 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl42 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")
        self.lbl51 = Label(self.master, text="", font=("Arial", 14), bg="red", fg="white", width=3,
                           borderwidth=2, relief="solid")

        self.lblRechenart1 = Label(self.master, text="+", font=("Arial", 14), bg="light green", fg="blue", width=1,
                           borderwidth=2, relief="sunken")
        self.lblRechenart2 = Label(self.master, text="+", font=("Arial", 14), bg="light green", fg="blue", width=1,
                           borderwidth=2, relief="sunken")
        self.lblRechenart3 = Label(self.master, text="+", font=("Arial", 14), bg="light green", fg="blue", width=1,
                                   borderwidth=2, relief="sunken")
        self.lblRechenart4 = Label(self.master, text="+", font=("Arial", 14), bg="light green", fg="blue", width=1,
                                   borderwidth=2, relief="sunken")

        self.lblWuerfelGroesse = Label(self.master, text="100", font=("Arial", 14), bg="grey", fg="white", width=3,
                                   borderwidth=2, relief="raised")

        self.lblRechenart1.grid(row=4, column=0, sticky=N + E + S + W)
        self.lblRechenart2.grid(row=3, column=0, sticky=N + E + S + W)
        self.lblRechenart3.grid(row=2, column=0, sticky=N + E + S + W)
        self.lblRechenart4.grid(row=1, column=0, sticky=N + E + S + W)
        self.lblWuerfelGroesse.grid(row=9, column=1, columnspan=2, sticky=N + E + S + W)

        self.lbl11.grid(row=5, column=1, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl12.grid(row=5, column=3, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl13.grid(row=5, column=5, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl14.grid(row=5, column=7, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl15.grid(row=5, column=9, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl21.grid(row=4, column=2, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl22.grid(row=4, column=4, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl23.grid(row=4, column=6, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl24.grid(row=4, column=8, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl31.grid(row=3, column=3, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl32.grid(row=3, column=5, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl33.grid(row=3, column=7, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl41.grid(row=2, column=4, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl42.grid(row=2, column=6, columnspan=2, sticky=N + E + S + W, ipadx=10)
        self.lbl51.grid(row=1, column=5, columnspan=2, sticky=N + E + S + W, ipadx=10)

        self.lbl21.bind("<Button-1>", self.gewaehltesFeld21)
        self.lbl22.bind("<Button-1>", self.gewaehltesFeld22)
        self.lbl23.bind("<Button-1>", self.gewaehltesFeld23)
        self.lbl24.bind("<Button-1>", self.gewaehltesFeld24)
        self.lbl31.bind("<Button-1>", self.gewaehltesFeld31)
        self.lbl32.bind("<Button-1>", self.gewaehltesFeld32)
        self.lbl33.bind("<Button-1>", self.gewaehltesFeld33)
        self.lbl41.bind("<Button-1>", self.gewaehltesFeld41)
        self.lbl42.bind("<Button-1>", self.gewaehltesFeld42)
        self.lbl51.bind("<Button-1>", self.gewaehltesFeld51)
        self.lblWuerfelGroesse.bind("<Button-1>", self.gewaehltesFeldWuerfelGroesse)

        self.but0 = Button(self.master, text="0", font=("Arial", 14), highlightbackground="grey", bg="grey", fg="white",
                      command=self.taste0)
        self.but1 = Button(self.master, text="1", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste1)
        self.but2 = Button(self.master, text="2", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste2)
        self.but3 = Button(self.master, text="3", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste3)
        self.but4 = Button(self.master, text="4", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste4)
        self.but5 = Button(self.master, text="5", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste5)
        self.but6 = Button(self.master, text="6", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste6)
        self.but7 = Button(self.master, text="7", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste7)
        self.but8 = Button(self.master, text="8", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste8)
        self.but9 = Button(self.master, text="9", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.taste9)
        self.butLoeschen = Button(self.master, text="<", font=("Arial", 14), highlightbackground="grey", bg="grey",
                            fg="white", command=self.tasteLoeschen)
        self.butNeuWuerfeln = Button(self.master, text="Neu", font=("Arial", 14), highlightbackground="grey", bg="grey",
                                  fg="white", command=self.neuWuerfeln)
        self.butMinus = Button(self.master, text="-", font=("Arial", 14), highlightbackground="grey", bg="grey",
                                     fg="white", command=self.tasteMinus)

        self.but0.grid(row=9, column=5, columnspan=2, sticky=W + E)
        self.but1.grid(row=8, column=3, columnspan=2, ipadx=10, sticky=W + E)
        self.but2.grid(row=8, column=5, columnspan=2, ipadx=10, sticky=W + E)
        self.but3.grid(row=8, column=7, columnspan=2, ipadx=10, sticky=W + E)
        self.but4.grid(row=7, column=3, columnspan=2, ipadx=10, sticky=W + E)
        self.but5.grid(row=7, column=5, columnspan=2, ipadx=10, sticky=W + E)
        self.but6.grid(row=7, column=7, columnspan=2, ipadx=10, sticky=W + E)
        self.but7.grid(row=6, column=3, columnspan=2, ipadx=10, sticky=W + E)
        self.but8.grid(row=6, column=5, columnspan=2, ipadx=10, sticky=W + E)
        self.but9.grid(row=6, column=7, columnspan=2, ipadx=10, sticky=W + E)
        self.butLoeschen.grid(row=9, column=9, columnspan=2, ipadx=10, sticky=W + E)
        self.butNeuWuerfeln.grid(row=9, column=3, columnspan=2, sticky=W + E)
        self.butMinus.grid(row=9, column=7, columnspan=2, ipadx=10, sticky=W + E)
        self.neuWuerfeln()
        self.master.mainloop()

    def richtigesErgebnis(self):
        exesStr = "if self.var" + str(self.gewaehltesFeld) + " == self.lbl" + str(
            self.gewaehltesFeld) + ".cget('text'): self.lbl" + \
                  str(self.gewaehltesFeld) + ".config(fg='blue')"
        try:
            exec(exesStr)
        except:
            pass

        exesStr = "if self.var" + str(self.gewaehltesFeld) + " != self.lbl" + str(
            self.gewaehltesFeld) + ".cget('text'): self.lbl" + \
                  str(self.gewaehltesFeld) + ".config(fg='white')"
        try:
            exec(exesStr)
        except:
            pass

        if self.lbl51.cget("fg") == "blue":
            self.lblWin = Label(self.master, text="Sie haben alle richtig gelöst!\nHerzlichen Glückwunsch!", font=("Arial", 14), bg="grey", fg="white", relief="raised")
            self.lblWin.grid(row=10, column=1, columnspan=10, ipadx=10, sticky=W + E)

    def gewaehltesFeld21(self, event):
        self.gewaehltesFeld = 21

    def gewaehltesFeld22(self, event):
        self.gewaehltesFeld = 22

    def gewaehltesFeld23(self, event):
        self.gewaehltesFeld = 23

    def gewaehltesFeld24(self, event):
        self.gewaehltesFeld = 24

    def gewaehltesFeld31(self, event):
        self.gewaehltesFeld = 31

    def gewaehltesFeld32(self, event):
        self.gewaehltesFeld = 32

    def gewaehltesFeld33(self, event):
        self.gewaehltesFeld = 33

    def gewaehltesFeld41(self, event):
        self.gewaehltesFeld = 41

    def gewaehltesFeld42(self, event):
        self.gewaehltesFeld = 42

    def gewaehltesFeld51(self, event):
        self.gewaehltesFeld = 51

    def gewaehltesFeldWuerfelGroesse(self, event):
        self.gewaehltesFeld = "WuerfelGroesse"


    def wertEinlesen(self):

        exesStr = "self.alterWert = str(self.lbl" + str(self.gewaehltesFeld) + ".cget('text'))"
        exec(exesStr)

    def wertSchreiben(self):
        execStr = "self.lbl" + str(self.gewaehltesFeld) + ".config(text=self.neuerWert)"
        exec(execStr)
        self.richtigesErgebnis()

    def taste0(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "0"
        self.wertSchreiben()

    def taste1(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "1"
        self.wertSchreiben()

    def taste2(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "2"
        self.wertSchreiben()

    def taste3(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "3"
        self.wertSchreiben()

    def taste4(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "4"
        self.wertSchreiben()

    def taste5(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "5"
        self.wertSchreiben()

    def taste6(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "6"
        self.wertSchreiben()

    def taste7(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "7"
        self.wertSchreiben()

    def taste8(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "8"
        self.wertSchreiben()

    def taste9(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "9"
        self.wertSchreiben()

    def tasteMinus(self):
        self.wertEinlesen()
        self.neuerWert = str(self.alterWert) + "-"
        self.wertSchreiben()

    def tasteLoeschen(self):
        self.wertEinlesen()
        alterWertListe = list(self.alterWert)
        try:
            alterWertListe.pop()
        except:
            pass
        self.neuerWert = ""
        for i in alterWertListe:
            self.neuerWert = self.neuerWert + i
        self.wertSchreiben()

    def neuWuerfeln(self):

        self.allesLoeschen()

        self.y = self.lblWuerfelGroesse.cget("text")

        if self.y == "" or self.y == "0":
            self.y = 100
        else:
            try:
                self.y = int(self.y)
            except:
                pass

        if self.y < 0:
            self.y = 100

        self.var11 = random.randint(1, self.y)
        self.var12 = random.randint(1, self.y)
        self.var13 = random.randint(1, self.y)
        self.var14 = random.randint(1, self.y)
        self.var15 = random.randint(1, self.y)

        self.lbl11.config(text=self.var11)
        self.lbl12.config(text=self.var12)
        self.lbl13.config(text=self.var13)
        self.lbl14.config(text=self.var14)
        self.lbl15.config(text=self.var15)

        self.randomVar = random.randint(1, 2)
        if self.randomVar == 1:
            self.additionEins()
        elif self.randomVar == 2:
            self.subtraktionEins()

        self.randomVar = random.randint(1, 2)
        if self.randomVar == 1:
            self.additionZwei()
        elif self.randomVar == 2:
            self.subtraktionZwei()

        self.randomVar = random.randint(1, 2)
        if self.randomVar == 1:
            self.additionDrei()
        elif self.randomVar == 2:
            self.subtraktionDrei()

        self.randomVar = random.randint(1, 2)
        if self.randomVar == 1:
            self.additionVier()
        elif self.randomVar == 2:
            self.subtraktionVier()


    def additionEins(self):
        self.var21 = str(self.var11 + self.var12)
        self.var22 = str(self.var12 + self.var13)
        self.var23 = str(self.var13 + self.var14)
        self.var24 = str(self.var14 + self.var15)

        self.lblRechenart1.config(text="+")

    def additionZwei(self):
        self.var31 = str(int(self.var21) + int(self.var22))
        self.var32 = str(int(self.var22) + int(self.var23))
        self.var33 = str(int(self.var23) + int(self.var24))

        self.lblRechenart2.config(text="+")

    def additionDrei(self):
        self.var41 = str(int(self.var31) + int(self.var32))
        self.var42 = str(int(self.var32) + int(self.var33))

        self.lblRechenart3.config(text="+")

    def additionVier(self):
        self.var51 = str(int(self.var41) + int(self.var42))

        self.lblRechenart4.config(text="+")

    def subtraktionEins(self):
        self.var21 = str(self.var11 - self.var12)
        self.var22 = str(self.var12 - self.var13)
        self.var23 = str(self.var13 - self.var14)
        self.var24 = str(self.var14 - self.var15)

        self.lblRechenart1.config(text="-")

    def subtraktionZwei(self):
        self.var31 = str(int(self.var21) - int(self.var22))
        self.var32 = str(int(self.var22) - int(self.var23))
        self.var33 = str(int(self.var23) - int(self.var24))

        self.lblRechenart2.config(text="-")

    def subtraktionDrei(self):
        self.var41 = str(int(self.var31) - int(self.var32))
        self.var42 = str(int(self.var32) - int(self.var33))

        self.lblRechenart3.config(text="-")

    def subtraktionVier(self):
        self.var51 = str(int(self.var41) - int(self.var42))

        self.lblRechenart4.config(text="-")

    def allesLoeschen(self):
        self.lbl21.config(text="", fg="white")
        self.lbl22.config(text="", fg="white")
        self.lbl23.config(text="", fg="white")
        self.lbl24.config(text="", fg="white")
        self.lbl31.config(text="", fg="white")
        self.lbl32.config(text="", fg="white")
        self.lbl33.config(text="", fg="white")
        self.lbl41.config(text="", fg="white")
        self.lbl42.config(text="", fg="white")
        self.lbl51.config(text="", fg="white")

        self.gewaehltesFeld = 21
        try:
            self.lblWin.destroy()
        except:
            pass

PyramidenRechnen()