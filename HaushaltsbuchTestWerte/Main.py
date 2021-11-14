from DatenVerwaltung import DatenVerwaltung as DV
from tkcalendar import DateEntry
from tkinter import *
import datetime, time
from datetime import datetime
from tkinter import font as tkFont
from tkinter import messagebox

class TkinterFenster():

    def __init__(self):
        Daten = DV()
        Daten.datenLaden()

        self.master = Tk()
        self.master.title("Haushaltsbuch")
        self.buchen = True



        # Variablen initalisieren

        self.summeBargeld = 0
        self.summeKreditkarte = 0
        self.summeGirokonto = 0
        self.summeSparkonto = 0

        # Font und Farben festlegen

        self.font01 = tkFont.Font(family="Arial", size=10)
        self.background = "lightgrey"
        self.foreground = "black"
        self.master.configure(background=self.background)
        self.master.resizable(width=False, height=False)
        self.colorNegativ = "red"
        self.colorPositiv = "green"
        self.colorNormal = "black"
        self.labelSorte = "ridge"

        # Labels

        Label(self.master, text="Datum", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=20).grid(row=1, column=1, sticky=N + E + S + W)
        Label(self.master, text="Betrag", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=20).grid(row=1, column=2, sticky=N + E + S + W)
        Label(self.master, text="Quellkonto", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=20).grid(row=1, column=3, sticky=N + E + S + W)
        Label(self.master, text="Zielkonto", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=20).grid(row=1, column=4, sticky=N + E + S + W)
        Label(self.master, text="Bezeichnung", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=20).grid(row=1, column=5, sticky=N + E + S + W)
        Label(self.master, text="Wiederholte Ausgaben", relief=self.labelSorte, bg=self.background,
              fg=self.foreground, font=self.font01, width=20).grid(row=8, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.master, text="Suchbegriff eingeben und Berechnen klicken:", relief=self.labelSorte, bg=self.background,
              fg=self.foreground, font=self.font01).grid(row=5, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.master, text="Konten:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=0, column=0, sticky=N + E + S + W)
        Label(self.master, text="alle\nBuchungen\nChronologisch:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=3, column=0, sticky=N + E + S + W)
        Label(self.master, text="Wiederholt\nMonatlich:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=7, column=0, sticky=N + E + S + W)
        Label(self.master, text="Wiederholt\nJährlich:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=9, column=0, sticky=N + E + S + W)
        Label(self.master, text="Bitte zu löschende Zeile eintragen:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=6, column=0, columnspan=2,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Tabelle wählen:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=6, column=3,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Wie viel\nnoch nicht\neingetragen ist:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, rowspan=3, column=0,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Ist Wert\neingetragen:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, rowspan=2, column=1,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Bargeld:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, column=2,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Kreditkarte:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, column=3,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Girokonto:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, column=4,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Sparkonto:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=10, column=5,
                                                                                  sticky=N + E + S + W)
        Label(self.master, text="Soll/Ist Abweichung:", relief=self.labelSorte,
              bg=self.background, fg=self.foreground, font=self.font01, width=12).grid(row=12, column=1,
                                                                                  sticky=N + E + S + W)

        # Entrys

        self.dateEntry01 = DateEntry(self.master, date_pattern='yyyy.mm.dd', font=self.font01)
        self.dateEntry01.grid(row=2, column=1, sticky=N + E + S + W)

        v1 = IntVar(self.master, value=0)
        self.entry01 = Entry(self.master, textvariable=v1, font=self.font01)
        self.entry01.grid(row=2, column=2, sticky=N + E + S + W)

        self.entry02 = Entry(self.master, font=self.font01)
        self.entry02.grid(row=2, column=5, sticky=N + E + S + W)

        self.entry03 = Entry(self.master, font=self.font01)
        self.entry03.grid(row=5, column=2, sticky=N + E + S + W)

        self.entry04 = Entry(self.master, font=self.font01)
        self.entry04.grid(row=6, column=2, sticky=N + E + S + W)

        v2 = IntVar(self.master, value=0)
        self.entry05 = Entry(self.master, textvariable=v2, font=self.font01)
        self.entry05.grid(row=11, column=2, sticky=N + E + S + W)

        v3 = IntVar(self.master, value=0)
        self.entry06 = Entry(self.master, textvariable=v3, font=self.font01)
        self.entry06.grid(row=11, column=3, sticky=N + E + S + W)

        v4 = IntVar(self.master, value=0)
        self.entry07 = Entry(self.master, textvariable=v4, font=self.font01)
        self.entry07.grid(row=11, column=4, sticky=N + E + S + W)

        v5 = IntVar(self.master, value=0)
        self.entry08 = Entry(self.master, textvariable=v5, font=self.font01)
        self.entry08.grid(row=11, column=5, sticky=N + E + S + W)

        # OptionMenu

        OptionenListe1 = [
            "Fremdkonto",
            "Bargeld",
            "Kreditkarte",
            "Girokonto",
            "Sparkonto"
        ]
        
        self.variable1 = StringVar(self.master)
        self.variable1.set(OptionenListe1[1])
        self.optionMenu01 = OptionMenu(self.master, self.variable1, *OptionenListe1)
        self.optionMenu01.grid(row=2, column=3, sticky=N + E + S + W)
        self.optionMenu01.config(font=self.font01)
        menu = self.master.nametowidget(self.optionMenu01.menuname)
        menu.config(font=self.font01)

        self.variable2 = StringVar(self.master)
        self.variable2.set(OptionenListe1[0])
        self.optionMenu02 = OptionMenu(self.master, self.variable2, *OptionenListe1)
        self.optionMenu02.grid(row=2, column=4, sticky=N + E + S + W)
        self.optionMenu02.config(font=self.font01)
        menu = self.master.nametowidget(self.optionMenu02.menuname)
        menu.config(font=self.font01)

        OptionenListe2 = [
            "aktuell",
            "Monatlich",
            "Jährlich"
        ]

        self.variable3 = StringVar(self.master)
        self.variable3.set(OptionenListe2[0])
        self.optionMenu03 = OptionMenu(self.master, self.variable3, *OptionenListe2)
        self.optionMenu03.grid(row=6, column=4, sticky=N + E + S + W)
        self.optionMenu03.config(font=self.font01)
        menu = self.master.nametowidget(self.optionMenu03.menuname)
        menu.config(font=self.font01)

        # Buttons

        self.button01 = Button(self.master, text="Buchen",
                               command=lambda: self.inListeEintragenMitUhrzeit(DV.ausgabenDatenListe),
                               bg=self.background, fg=self.foreground, font=self.font01)
        self.button01.grid(row=2, column=6, sticky=N + E + S + W)

        self.button02 = Button(self.master, text="letzte Buchung\n löschen",
                               command=self.eintragLoeschen, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button02.grid(row=4, column=6, sticky=N + E + S + W)

        self.button03 = Button(self.master, text="Speichern", command=Daten.datenSpeichern,
                               bg=self.background, fg=self.foreground, font=self.font01)
        self.button03.grid(row=1, column=6, sticky=N + E + S + W)

        self.button04 = Button(self.master, text="Monatlich Wiederholte \n nach oben Übertragen", command=self.uebertragenMonatlich,
                               bg=self.background, fg=self.foreground, font=self.font01)
        self.button04.grid(row=8, column=4, sticky=N + E + S + W)

        self.button05 = Button(self.master, text="Monatliche\nWiederholung\nBuchen",
                               command=lambda: self.inListeEintragenOhneUhrzeit(DV.ausgabenMonatlichWiederholtDatenListe), bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button05.grid(row=5, column=6, rowspan=2, sticky=N + E + S + W)

        self.button06 = Button(self.master, text=" letzte Buchung\n löschen",
                               command=self.eintragWiederholtLoeschen, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button06.grid(row=7, column=6, sticky=N + E + S + W)

        self.button07 = Button(self.master, text="Monatlich Wiederholte\n oben löschen",
                               command=self.aktuelleMinusRegelmaessigeMonatlich, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button07.grid(row=8, column=5, sticky=N + E + S + W)

        self.button08 = Button(self.master, text="Berechnen",
                               command=self.berechnungSuchbegriff, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button08.grid(row=5, column=5, sticky=N + E + S + W)

        self.button09 = Button(self.master, text="Beenden",
                               command=self.beendenFenster, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button09.grid(row=0, column=6, sticky=N + E + S + W)

        self.button10 = Button(self.master, text="Jährliche\nWiederholung\nBuchen",
                               command=lambda: self.inListeEintragenOhneUhrzeit(DV.ausgabenJaehrlichWiederholtDatenListe),
                               bg=self.background, fg=self.foreground, font=self.font01)
        self.button10.grid(row=8, column=6, sticky=N + E + S + W)

        self.button11 = Button(self.master, text="letzte Buchung\nlöschen",
                               command=self.eintragJaehrlichWiederholtLoeschen, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button11.grid(row=9, column=6, sticky=N + E + S + W)

        self.button12 = Button(self.master, text="Jährlich Wiederholte\nnach oben übertragen",
                               command=self.uebertragenJaehrlich, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button12.grid(row=8, column=2, sticky=N + E + S + W)

        self.button13 = Button(self.master, text="Jährlich Wiederholt\noben löschen",
                               command=self.aktuelleMinusRegelmaessigeJaehrlich, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button13.grid(row=8, column=3, sticky=N + E + S + W)

        self.button14 = Button(self.master, text="Löschen",
                               command=self.zeileLoeschen, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button14.grid(row=6, column=5, sticky=N + E + S + W)

        self.button15 = Button(self.master, text="Berechnen",
                               command=self.berechnungUndDarstellungDerKontoAbweichung, bg=self.background,
                               fg=self.foreground, font=self.font01)
        self.button15.grid(row=10, rowspan=3, column=6, sticky=N + E + S + W)

        # Textfelder + Scrollbars

        self.textfeld1 = Text(self.master, height=15, width=120, font=self.font01)
        self.textfeld1.grid(row=3, column=1, rowspan=2, columnspan=5, sticky=W)
        self.scrollbar1 = Scrollbar(self.master)
        self.scrollbar1.grid(row=3, column=5, rowspan=2, sticky=N + E + S)
        self.textfeld1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textfeld1.yview)

        self.textfeld2 = Text(self.master, height=10, width=120, font=self.font01)
        self.textfeld2.grid(row=7, column=1, rowspan=1, columnspan=5, sticky=W)
        self.scrollbar2 = Scrollbar(self.master)
        self.scrollbar2.grid(row=7, column=5, rowspan=1, sticky=N + E + S)
        self.textfeld2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.textfeld2.yview)

        self.textfeld3 = Text(self.master, height=5, width=120, font=self.font01)
        self.textfeld3.grid(row=9, column=1, rowspan=1, columnspan=5, sticky=W)
        self.scrollbar3 = Scrollbar(self.master)
        self.scrollbar3.grid(row=9, column=5, rowspan=1, sticky=N + E + S)
        self.textfeld3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.textfeld3.yview)

        # Computed Labels

        self.label01 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label01.grid(row=0, column=1, sticky=N + E + S + W)

        self.label02 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label02.grid(row=0, column=2, sticky=N + E + S + W)

        self.label03 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label03.grid(row=0, column=3, sticky=N + E + S + W)

        self.label04 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label04.grid(row=0, column=4, sticky=N + E + S + W)

        self.label05 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label05.grid(row=5, column=3, columnspan=2, sticky=N + E + S + W)

        self.label06 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground, font=self.font01)
        self.label06.grid(row=0, column=5, sticky=N + E + S + W)

        self.label07 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                             font=self.font01)
        self.label07.grid(row=12, column=2, sticky=N + E + S + W)

        self.label08 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                             font=self.font01)
        self.label08.grid(row=12, column=3, sticky=N + E + S + W)

        self.label09 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                             font=self.font01)
        self.label09.grid(row=12, column=4, sticky=N + E + S + W)

        self.label10 = Label(self.master, text="", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                             font=self.font01)
        self.label10.grid(row=12, column=5, sticky=N + E + S + W)

        self.berechnungUndDarstellungDerKonten()
        self.master.mainloop()



    def beendenFenster(self):

        # BeendenFenster öffnen

        self.antwort = messagebox.askokcancel("Beenden?", "Wollen Sie wirklich\ndas Programm beenden?\nNicht gespeicherte Inhalte\ngehen verloren!")
        if self.antwort == True:
            self.master.quit()

    def zeileLoeschen(self):

        # löschen einer Zeile in einer der drei Listen mit Auswahl und überprüfen ob wirklich ein Int eingetragen wird

        self.stringToInt(self.entry04.get())
        if self.buchen:
            if self.variable3.get() == "aktuell":
                del DV.ausgabenDatenListe[self.stringToInt(self.entry04.get())]
                self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe,
                                       self.colorNegativ, self.colorPositiv, self.colorNormal)
            if self.variable3.get() == "Monatlich":
                del DV.ausgabenMonatlichWiederholtDatenListe[self.stringToInt(self.entry04.get())]
                self.textfelderFuellen(self.textfeld2, DV.ausgabenMonatlichWiederholtDatenListe,
                                       self.colorNegativ, self.colorPositiv, self.colorNormal)
            if self.variable3.get() == "Jährlich":
                del DV.ausgabenJaehrlichWiederholtDatenListe[self.stringToInt(self.entry04.get())]
                self.textfelderFuellen(self.textfeld3, DV.ausgabenJaehrlichWiederholtDatenListe,
                                       self.colorNegativ, self.colorPositiv, self.colorNormal)

        # nach dem Löschen neudarstellung der Konten

        self.berechnungUndDarstellungDerKonten()

    def ausgabenListenSortieren(self):

        # alle drei Listen absteigend sortieren

        DV.ausgabenDatenListe.sort(reverse=True)
        DV.ausgabenMonatlichWiederholtDatenListe.sort(reverse=True)
        DV.ausgabenJaehrlichWiederholtDatenListe.sort(reverse=True)

    def replaceCommaWithPoint(self, wertStr):

        # Kommas mit Punkten austauschen um Berechnungen durchzuführen

        wertStr = wertStr.replace(",", ".")
        return wertStr

    def stringToInt(self, wertStr):

        # String to Int mit Überprüfen beim Buchen ob wirklich eine Zahl eingetragen ist

        wertInt = 0
        try:
            wertInt = int(wertStr)
            self.buchen = True
        except:
            messagebox.showwarning("Bitte nur Zahlen eintragen!")
            self.buchen = False
        return wertInt

    def stringToFloat(self, wertStr):

        # String to Float mit Überprüfen beim Buchen ob wirklich eine Zahl eingetragen ist

        wertFloat = 0
        try:
            wertFloat = float(wertStr)
            self.buchen = True
        except:
            messagebox.showwarning("Bitte eine Zahl eintragen!")
            self.buchen = False
        return wertFloat

    def textfelderFuellen(self, textfeld, liste, colorNegativ, colorPositiv, colorNormal):

        # Füllen eines Textfeldes, das Textfeld und die Liste plus die Farben muss übergeben werden.

        # Übername der Variablen

        self.textfeld = textfeld
        self.liste = liste
        self.colorNegativ = colorNegativ
        self.colorPositiv = colorPositiv
        self.colorNormal = colorNormal

        # Freischalten des Textfeldes, sortieren der Liste nach Dadum und löschen des Textfeldes

        self.textfeld.config(state="normal")
        self.ausgabenListenSortieren()
        self.textfeld.delete(1.0, END)

        # durchlaufen der Liste und schreiben ins Textfeld, die Floats(Euro Werte) werden farblich markiert

        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if j == 0:
                    if i < 10:
                        self.textfeld.insert(END, "00")
                    elif i < 100:
                        self.textfeld.insert(END, "0")
                    self.textfeld.insert(END, i)
                self.textfeld.insert(END, "   |   ")
                try:
                    float(self.liste[i][j])
                    if float(self.liste[i][j]) < 0:
                        self.textfeld.tag_config(str(self.liste[i][j]), foreground=self.colorNegativ)
                        self.textfeld.insert(END, str(round(float(self.liste[i][j]), 2)) + " €", str(self.liste[i][j]))
                    else:
                        self.textfeld.tag_config(str(self.liste[i][j]), foreground=self.colorPositiv)
                        self.textfeld.insert(END, " " + str(round(float(self.liste[i][j]), 2)) + " €", str(self.liste[i][j]))
                except:
                    self.textfeld.tag_config(str(self.liste[i][j]), foreground=self.colorNormal)
                    self.textfeld.insert(END, self.liste[i][j], str(self.liste[i][j]))
                self.textfeld.insert(END, "\t\t")
            self.textfeld.insert(END, "\n")

        self.textfeld.config(state="disabled")

    def berechnungSuchbegriff(self):

        # Lesen und Aufsummierung des Suchbegriffes und anschließende Ausgabe

        summeEntry03 = 0
        for i in range(len(DV.ausgabenDatenListe)):
            wertStr = self.replaceCommaWithPoint(DV.ausgabenDatenListe[i][2])
            if DV.ausgabenDatenListe[i][5] == self.entry03.get():
                summeEntry03 = summeEntry03 + self.stringToFloat(wertStr)

        if summeEntry03 < 0:
            entry03SummeStr = "Summe " + self.entry03.get() + ": " + str(round(summeEntry03, 2))
            self.label05.config(text=entry03SummeStr, fg=self.colorNegativ)
        else:
            entry03SummeStr = "Summe " + self.entry03.get() + ": " + str(round(summeEntry03, 2))
            self.label05.config(text=entry03SummeStr, fg=self.colorPositiv)

    def berechnungUndDarstellungDerKontoAbweichung(self):

        # Kontoabweichung berechnen und in Labels ausgeben, um schnell die Differenz zu erfassen,
        # um zu sehen wo noch Buchungen fehlen

        self.label07.config(text=str(round(self.summeBargeld - float(self.replaceCommaWithPoint(self.entry05.get())), 2)))
        self.label08.config(text=str(round(self.summeKreditkarte - float(self.replaceCommaWithPoint(self.entry06.get())), 2)))
        self.label09.config(text=str(round(self.summeGirokonto - float(self.replaceCommaWithPoint(self.entry07.get())), 2)))
        self.label10.config(text=str(round(self.summeSparkonto - float(self.replaceCommaWithPoint(self.entry08.get())), 2)))

    def berechnungUndDarstellungDerKonten(self):

        # Setzen der Konten auf 0

        self.summeBargeld = 0
        self.summeKreditkarte = 0
        self.summeGirokonto = 0
        self.summeSparkonto = 0

        # Neu laden der Textfelder

        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe,
                               self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.textfelderFuellen(self.textfeld2, DV.ausgabenMonatlichWiederholtDatenListe,
                               self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.textfelderFuellen(self.textfeld3, DV.ausgabenJaehrlichWiederholtDatenListe,
                               self.colorNegativ, self.colorPositiv, self.colorNormal)

        # Herraussuchen der Konten und aufsummieren der Einnahmen/Ausgaben

        for i in range(len(DV.ausgabenDatenListe)):
            wertStr = self.replaceCommaWithPoint(DV.ausgabenDatenListe[i][2])
            if DV.ausgabenDatenListe[i][3] == "Bargeld":
                if float(DV.ausgabenDatenListe[i][2]) < 0:
                    self.summeBargeld = self.summeBargeld + self.stringToFloat(wertStr)
                else:
                    self.summeBargeld = self.summeBargeld - self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][4] == "Bargeld":
                self.summeBargeld = self.summeBargeld + self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][3] == "Kreditkarte":
                if float(DV.ausgabenDatenListe[i][2]) < 0:
                    self.summeKreditkarte = self.summeKreditkarte + self.stringToFloat(wertStr)
                else:
                    self.summeKreditkarte = self.summeKreditkarte - self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][4] == "Kreditkarte":
                self.summeKreditkarte = self.summeKreditkarte + self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][3] == "Girokonto":
                if float(DV.ausgabenDatenListe[i][2]) < 0:
                    self.summeGirokonto = self.summeGirokonto + self.stringToFloat(wertStr)
                else:
                    self.summeGirokonto = self.summeGirokonto - self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][4] == "Girokonto":
                self.summeGirokonto = self.summeGirokonto + self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][3] == "Sparkonto":
                if float(DV.ausgabenDatenListe[i][2]) < 0:
                    self.summeSparkonto = self.summeSparkonto + self.stringToFloat(wertStr)
                else:
                    self.summeSparkonto = self.summeSparkonto - self.stringToFloat(wertStr)
            if DV.ausgabenDatenListe[i][4] == "Sparkonto":
                self.summeSparkonto = self.summeSparkonto + self.stringToFloat(wertStr)

        # Aufsummieren aller Konten

        self.berechnungSumme = self.summeBargeld + self.summeKreditkarte + self.summeGirokonto + self.summeSparkonto

        # Ausgabe der Konten in die Kontolabels

        if self.berechnungSumme < 0:
            berechnungSummeStr = "Gesammt: " + str(round(self.berechnungSumme, 2))
            self.label01.config(text=berechnungSummeStr, fg=self.colorNegativ)
        else:
            berechnungSummeStr = "Gesammt: " + str(round(self.berechnungSumme, 2))
            self.label01.config(text=berechnungSummeStr, fg=self.colorPositiv)

        if self.summeBargeld < 0:
            bargeldSummeStr = "Bargeld: " + str(round(self.summeBargeld, 2))
            self.label02.config(text=bargeldSummeStr, fg=self.colorNegativ)
        else:
            bargeldSummeStr = "Bargeld: " + str(round(self.summeBargeld, 2))
            self.label02.config(text=bargeldSummeStr, fg=self.colorPositiv)

        if self.summeKreditkarte < 0:
            kreditkartenSummeStr = "Kreditkarte: " + str(round(self.summeKreditkarte, 2))
            self.label03.config(text=kreditkartenSummeStr, fg=self.colorNegativ)
        else:
            kreditkartenSummeStr = "Kreditkarte: " + str(round(self.summeKreditkarte, 2))
            self.label03.config(text=kreditkartenSummeStr, fg=self.colorPositiv)

        if self.summeGirokonto < 0:
            girokontoSummeStr = "Girokonto: " + str(round(self.summeGirokonto, 2))
            self.label04.config(text=girokontoSummeStr, fg=self.colorNegativ)
        else:
            girokontoSummeStr = "Girokonto: " + str(round(self.summeGirokonto, 2))
            self.label04.config(text=girokontoSummeStr, fg=self.colorPositiv)

        if self.summeSparkonto < 0:
            sparkontoSummeStr = "Sparkonto: " + str(round(self.summeSparkonto, 2))
            self.label06.config(text=sparkontoSummeStr, fg=self.colorNegativ)
        else:
            sparkontoSummeStr = "Sparkonto: " + str(round(self.summeSparkonto, 2))
            self.label06.config(text=sparkontoSummeStr, fg=self.colorPositiv)

    def inListeEintragenMitUhrzeit(self, liste):

        # In die übergebene Liste eintragen mit genauem Datum und Uhrzeit

        self.liste = liste
        lt = time.localtime()
        self.stringToFloat(self.replaceCommaWithPoint(self.entry01.get()))
        if self.buchen:
            neuerDatensatz = [self.dateEntry01.get(), time.strftime("%H:%M:%S", lt), self.replaceCommaWithPoint(self.entry01.get()), self.variable1.get(), self.variable2.get(), self.entry02.get()]
            self.liste.append(neuerDatensatz)
            self.berechnungUndDarstellungDerKonten()

    def inListeEintragenOhneUhrzeit(self, liste):

        # In die übergebene Liste eintragen mit genauem Datum ohne Uhrzeit
        # (damit man den Unterschied zwischen aktuellen Buchungen und Fixkosten sieht)

        self.liste = liste
        timeTupel = 2000, 0, 0, 0, 0, 0, 0, 0, 0
        self.stringToFloat(self.replaceCommaWithPoint(self.entry01.get()))
        if self.buchen:
            neuerDatensatz = [self.dateEntry01.get(), time.strftime("%H:%M:%S", timeTupel), self.replaceCommaWithPoint(self.entry01.get()), self.variable1.get(), self.variable2.get(), self.entry02.get()]
            self.liste.append(neuerDatensatz)
            self.berechnungUndDarstellungDerKonten()

    def eintragLoeschen(self):

        # "obersten" Eintrag in der aktuellen Liste löschen

        del DV.ausgabenDatenListe[0]
        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def eintragWiederholtLoeschen(self):

        # "obersten" Eintrag in der Monatlichen Liste löschen

        del DV.ausgabenMonatlichWiederholtDatenListe[0]
        self.textfelderFuellen(self.textfeld2, DV.ausgabenMonatlichWiederholtDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def eintragJaehrlichWiederholtLoeschen(self):

        # "obersten" Eintrag in der Jährlichen Liste löschen

        del DV.ausgabenJaehrlichWiederholtDatenListe[0]
        self.textfelderFuellen(self.textfeld3, DV.ausgabenJaehrlichWiederholtDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def uebertragenMonatlich(self):

        # Monatliche Fixkosten in die aktuelle Liste übertragen, vorher die Daten des Monats aktualisieren
        # und überprüfen ob die Fixkosten schon vorhanden sind

        self.monatAktuallisieren()
        if [elem for elem in DV.ausgabenMonatlichWiederholtDatenListe if elem not in DV.ausgabenDatenListe]:
            DV.ausgabenDatenListe = [elem for elem in DV.ausgabenDatenListe if
                                     elem not in DV.ausgabenMonatlichWiederholtDatenListe]
            DV.ausgabenDatenListe = DV.ausgabenDatenListe + DV.ausgabenMonatlichWiederholtDatenListe
        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def uebertragenJaehrlich(self):

        # Jährliche Fixkosten in die aktuelle Liste übertragen, vorher die Daten des Jahres aktualisieren
        # und überprüfen ob die Fixkosten schon vorhanden sind

        self.jaehrlichAktuallisieren()
        if [elem for elem in DV.ausgabenJaehrlichWiederholtDatenListe if elem not in DV.ausgabenDatenListe]:
            DV.ausgabenDatenListe = [elem for elem in DV.ausgabenDatenListe if
                                     elem not in DV.ausgabenJaehrlichWiederholtDatenListe]
            DV.ausgabenDatenListe = DV.ausgabenDatenListe + DV.ausgabenJaehrlichWiederholtDatenListe
        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def monatAktuallisieren(self):

        # Monatliche Daten aktuallisieren, dafür werden die Jahre und der Monat auf das jetztige gestellt

        for i in range(len(DV.ausgabenMonatlichWiederholtDatenListe)):
            my_date = datetime.strptime(DV.ausgabenMonatlichWiederholtDatenListe[i][0], "%Y.%m.%d")
            my_date = my_date.replace(month=datetime.today().month)
            my_date = my_date.replace(year=datetime.today().year)
            DV.ausgabenMonatlichWiederholtDatenListe[i][0] = datetime.strftime(my_date, "%Y.%m.%d")

    def jaehrlichAktuallisieren(self):

        # Jährliche Daten aktuallisieren, dafür werden die Jahre auf das jetztige gestellt

        for i in range(len(DV.ausgabenJaehrlichWiederholtDatenListe)):
            my_date = datetime.strptime(DV.ausgabenJaehrlichWiederholtDatenListe[i][0], "%Y.%m.%d")
            my_date = my_date.replace(year=datetime.today().year)
            DV.ausgabenJaehrlichWiederholtDatenListe[i][0] = datetime.strftime(my_date, "%Y.%m.%d")

    def aktuelleMinusRegelmaessigeMonatlich(self):

        # alle Monatlichen aus der aktuellen Liste löschen

        self.monatAktuallisieren()
        DV.ausgabenDatenListe = [elem for elem in DV.ausgabenDatenListe if elem not in DV.ausgabenMonatlichWiederholtDatenListe]
        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()

    def aktuelleMinusRegelmaessigeJaehrlich(self):

        # alle Jährlichen aus der aktuellen Liste löschen

        self.jaehrlichAktuallisieren()
        DV.ausgabenDatenListe = [elem for elem in DV.ausgabenDatenListe if elem not in DV.ausgabenJaehrlichWiederholtDatenListe]
        self.textfelderFuellen(self.textfeld1, DV.ausgabenDatenListe, self.colorNegativ, self.colorPositiv, self.colorNormal)
        self.berechnungUndDarstellungDerKonten()


def main():

    TkF = TkinterFenster()

if __name__=="__main__":
    main()



