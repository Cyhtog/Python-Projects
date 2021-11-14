from tkinter import *

class Taschenrechner():
    def __init__(self):
        self.rechenart = "keine"
        self.wert = ""
        self.master = Tk()
        self.master.title("Taschenrechner")
        self.master.resizable(width=False, height=False)

        self.lbl1 = Label(self.master, text="", font=("Arial", 14), anchor="e", bg="white", fg="blue")
        self.lbl2 = Label(self.master, text="", font=("Arial", 14), anchor="e", bg="white", fg="blue")
        self.lbl3 = Label(self.master, text="", font=("Arial", 14), anchor="e", bg="white", fg="blue")
        self.lbl4 = Label(self.master, text="", font=("Arial", 14), bg="white", fg="blue")
        self.lbl5 = Label(self.master, text="", font=("Arial", 14), bg="white", fg="blue")
        self.lbl1.grid(row=0, column=0, columnspan=5, sticky=W + E)
        self.lbl2.grid(row=1, column=0, columnspan=5, sticky=W + E)
        self.lbl3.grid(row=2, column=1, columnspan=4, sticky=W + E)
        self.lbl4.grid(row=1, column=0, sticky=W + E)
        self.lbl5.grid(row=2, column=0, sticky=W + E)

        self.but1 = Button(self.master, text="0", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste0)
        self.but2 = Button(self.master, text="1", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste1)
        self.but3 = Button(self.master, text="2", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste2)
        self.but4 = Button(self.master, text="3", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste3)
        self.but5 = Button(self.master, text="4", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste4)
        self.but6 = Button(self.master, text="5", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste5)
        self.but7 = Button(self.master, text="6", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste6)
        self.but8 = Button(self.master, text="7", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste7)
        self.but9 = Button(self.master, text="8", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                      command=self.taste8)
        self.but10 = Button(self.master, text="9", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.taste9)
        self.but11 = Button(self.master, text="+", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.addition)
        self.but12 = Button(self.master, text="-", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.subtration)
        self.but13 = Button(self.master, text="*", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.multiplikation)
        self.but14 = Button(self.master, text="/", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.division)
        self.but15 = Button(self.master, text="=", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.berechnen)
        self.but16 = Button(self.master, text=",", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteKomma)
        self.but17 = Button(self.master, text="<", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.loeschen)
        self.but18 = Button(self.master, text="CE", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteCE)
        self.but19 = Button(self.master, text="C", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteC)
        self.but20 = Button(self.master, text="M1", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteM1)
        self.but21 = Button(self.master, text="M1+", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteM1_)
        self.but22 = Button(self.master, text="M2+", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteM2_)
        self.but23 = Button(self.master, text="M2", font=("Arial", 14), highlightbackground="blue", bg="blue", fg="white",
                       command=self.tasteM2)

        self.but1.grid(row=7, column=0, columnspan=2, sticky=W + E)
        self.but2.grid(row=6, column=0, ipadx=10)
        self.but3.grid(row=6, column=1, ipadx=10)
        self.but4.grid(row=6, column=2, ipadx=10)
        self.but5.grid(row=5, column=0, ipadx=10)
        self.but6.grid(row=5, column=1, ipadx=10)
        self.but7.grid(row=5, column=2, ipadx=10)
        self.but8.grid(row=4, column=0, ipadx=10)
        self.but9.grid(row=4, column=1, ipadx=10)
        self.but10.grid(row=4, column=2, ipadx=10)
        self.but11.grid(row=7, column=3, ipadx=10)
        self.but12.grid(row=6, column=3, sticky=W + E)
        self.but13.grid(row=5, column=3, sticky=W + E)
        self.but14.grid(row=4, column=3, sticky=W + E)
        self.but15.grid(row=6, column=4, sticky=N + S + W + E, rowspan=2)
        self.but16.grid(row=7, column=2, sticky=W + E)
        self.but17.grid(row=3, column=0, sticky=W + E)
        self.but18.grid(row=3, column=1, sticky=W + E)
        self.but19.grid(row=3, column=2, sticky=W + E)
        self.but20.grid(row=3, column=3, sticky=W + E)
        self.but21.grid(row=4, column=4, sticky=W + E)
        self.but22.grid(row=5, column=4, sticky=W + E)
        self.but23.grid(row=3, column=4, sticky=W + E)

        self.master.mainloop()

    def taste0(self):
        if self.wertEinlesenStr(self.lbl3.cget("text")) == "0":
            pass
        else:
            self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
            self.wert = self.wertAusgabe(self.wert + self.but1.cget("text"))
            self.lbl3.config(text=self.wert)

    def taste1(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but2.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste2(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but3.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste3(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but4.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste4(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but5.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste5(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but6.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste6(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but7.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste7(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but8.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste8(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but9.cget("text"))
        self.lbl3.config(text=self.wert)

    def taste9(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wertAusgabe(self.wert + self.but10.cget("text"))
        self.lbl3.config(text=self.wert)

    def tasteKomma(self):
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wert = self.wert + self.but16.cget("text")
        self.lbl3.config(text=self.wert)

    def tasteC(self):
        self.lbl1.config(text="")
        self.lbl2.config(text="")
        self.lbl3.config(text="")
        self.lbl4.config(text="")
        self.lbl5.config(text="")

    def tasteCE(self):
        self.lbl3.config(text="")
        self.lbl4.config(text="")
        self.lbl5.config(text="")

    def tasteM1(self):
        self.m1 = self.lbl3.cget("text")

    def tasteM2(self):
        self.m2 = self.lbl3.cget("text")

    def tasteM1_(self):
        self.lbl3.config(text=self.m1)

    def tasteM2_(self):
        self.lbl3.config(text=self.m2)

    def loeschen(self):
        self.wertStr = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wertListe = list(self.wertStr)
        self.wertListe.pop()
        self.wertStr = ""
        for i in self.wertListe:
            self.wertStr = self.wertStr + i
        self.wertAusgeben = self.wertAusgabe(self.wertStr)
        self.lbl3.config(text=self.wertAusgeben)

    def addition(self):
        self.rechenart = "addition"
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wertStr = self.wertAusgabe(self.wert)
        self.lbl1.config(text=self.lbl2.cget("text"))
        self.lbl2.config(text=self.wertStr)
        self.lbl3.config(text="")
        self.lbl4.config(text="+")

    def subtration(self):
        self.rechenart = "subtration"
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wertStr = self.wertAusgabe(self.wert)
        self.lbl1.config(text=self.lbl2.cget("text"))
        self.lbl2.config(text=self.wertStr)
        self.lbl3.config(text="")
        self.lbl4.config(text="-")

    def multiplikation(self):
        self.rechenart = "multiplikation"
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wertStr = self.wertAusgabe(self.wert)
        self.lbl1.config(text=self.lbl2.cget("text"))
        self.lbl2.config(text=self.wertStr)
        self.lbl3.config(text="")
        self.lbl4.config(text="*")

    def division(self):
        self.rechenart = "division"
        self.wert = self.wertEinlesenStr(self.lbl3.cget("text"))
        self.wertStr = self.wertAusgabe(self.wert)
        self.lbl1.config(text=self.lbl2.cget("text"))
        self.lbl2.config(text=self.wertStr)
        self.lbl3.config(text="")
        self.lbl4.config(text="/")

    def berechnen(self):
        if self.lbl4.cget("text") == "":
            print("Zuerst Zahlen eingeben, oder Rechenart wählen!")
        else:
            self.ergebnisFloat = 0.0
            try:
                self.ersterWertFloat = self.wertEinlesenFloat(self.lbl2.cget("text"))
                self.zweiterWertFloat = self.wertEinlesenFloat(self.lbl3.cget("text"))
            except:
                self.ersterWertFloat = 0.0
                self.zweiterWertFloat = 0.0

            if self.rechenart == "addition":
                self.ergebnisFloat = self.ersterWertFloat + self.zweiterWertFloat
            elif self.rechenart == "subtration":
               self.ergebnisFloat = self.ersterWertFloat - self.zweiterWertFloat
            elif self.rechenart == "multiplikation":
                self.ergebnisFloat = self.ersterWertFloat * self.zweiterWertFloat
            elif self.rechenart == "division":
                try:
                    self.ergebnisFloat = self.ersterWertFloat / self.zweiterWertFloat
                except:
                    print("Division durch 0 nicht möglich")
            if self.rechenart == "division" and self.zweiterWertFloat == 0:
                self.lbl3.config(text="Division durch\n0 nicht möglich!")
            else:
                self.ergebnisFloat = round(self.ergebnisFloat, 10)
                self.wertStr = self.wertEinlesenStr(self.lbl2.cget("text"))
                self.wertStr = self.wertAusgabe(self.wertStr)
                self.lbl1.config(text=(self.wertStr))
                self.wertStr = self.wertEinlesenStr(self.lbl3.cget("text"))
                self.wertStr = self.wertAusgabe(self.wertStr)
                self.lbl2.config(text=(self.wertStr))
                self.ergebnisStr = self.wertAusgabe(self.ergebnisFloat)
                self.lbl3.config(text=self.ergebnisStr)
                self.lbl5.config(text="=")

    def wertEinlesenStr(self, wert):
        self.wertStr = wert.replace(".", "")
        self.wertStr = self.wertStr.replace(",", ".")
        return self.wertStr

    def wertEinlesenFloat(self, wert):
        self.wertStr = wert.replace(".", "")
        self.wertStr = self.wertStr.replace(",", ".")
        try:
            self.wertFloat = float(self.wertStr)
        except:
            print("Fehler beim wert Einlesen")
        return self.wertFloat

    def wertAusgabe(self, wert):
        try:
            self.wertStr = str(wert)
        except:
            print("Fehler beim Stringumwandlung")
        self.wertListe = list(self.wertStr)
        if 15 < len(self.wertListe):
            print(self.wert)
            self.lbl3.config(text="Wert zu groß")
        else:
            self.wertStr = self.wertStr.replace(".", ",")
            self.wertStrPartitioniert = self.wertStr.partition(",")
            self.wertListLinks = list(self.wertStrPartitioniert[0])
            self.wertListLinks.reverse()
            self.drehen = "j"
            self.wertStrLinks = self.tausenderPunkt(self.wertListLinks, self.drehen)

            self.wertListRechts = list(self.wertStrPartitioniert[2])
            self.drehen= "n"
            self.wertStrRechts = self.tausenderPunkt(self.wertListRechts, self.drehen)
            try:
                self.wertIntRechts = int(self.wertStrRechts)
            except:
                self.wertIntRechts = 1

            if self.wertIntRechts == 0:
                self.wertStr = self.wertStrLinks
            else:
                self.wertStr = self.wertStrLinks + self.wertStrPartitioniert[1] + self.wertStrRechts
            return self.wertStr

    def tausenderPunkt(self, ergebnisList, drehen):
        self.charakterZähler = 0
        self.ergebnisStr = ""
        for i in ergebnisList:
            if self.charakterZähler == 3:
                self.ergebnisStr = self.ergebnisStr + "." + i
                self.charakterZähler = 1
            else:
                self.ergebnisStr = self.ergebnisStr + i
                self.charakterZähler = self.charakterZähler + 1
        if drehen == "j":
            self.ergebnisList = list(self.ergebnisStr)
            self.ergebnisList.reverse()
            self.ergebnisStr = ""
            for self.i in self.ergebnisList:
                self.ergebnisStr = self.ergebnisStr + self.i
        return self.ergebnisStr

def main():
    Taschenrechner()

if __name__=="__main__":
    main()