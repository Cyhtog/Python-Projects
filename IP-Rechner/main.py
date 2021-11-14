from tkinter import *
from ui_main import UI_MainWindow
import ipaddress


class TkinterFenster(Tk, UI_MainWindow):

    def __init__(self):
        super(TkinterFenster, self).__init__()
        self.setup()

        self.ipSplit()

        self.entry01.bind('<Return>', lambda e: self.ipSplit())
        self.entry02.bind('<Return>', lambda e: self.cidrSuffixZuNetzwerkmaske())
        self.entry03.bind('<Return>', lambda e: self.netzwerkmaskeZuCIDRSuffix())

    def dezimalZuBinär(self):

        # erster Teil der IP

        try:
            zahl = int(self.label1.cget("text"))
        except:
            zahl = -1
            self.labelWarnung1.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        if 0 <= zahl < 256:
            self.labelWarnung1.config(text="")

            zahlMinus128 = zahl - 128
            if zahlMinus128 >= 0:
                self.checkbutton1_128.select()
                self.label1_128.config(text="1")
                zahl = zahlMinus128
            else:
                self.label1_128.config(text="0")
                self.checkbutton1_128.deselect()

            zahlMinus64 = zahl - 64
            if zahlMinus64 >= 0:
                self.checkbutton1_64.select()
                self.label1_64.config(text="1")
                zahl = zahlMinus64
            else:
                self.label1_64.config(text="0")
                self.checkbutton1_64.deselect()

            zahlMinus32 = zahl - 32
            if zahlMinus32 >= 0:
                self.checkbutton1_32.select()
                self.label1_32.config(text="1")
                zahl = zahlMinus32
            else:
                self.label1_32.config(text="0")
                self.checkbutton1_32.deselect()

            zahlMinus16 = zahl - 16
            if zahlMinus16 >= 0:
                self.checkbutton1_16.select()
                self.label1_16.config(text="1")
                zahl = zahlMinus16
            else:
                self.label1_16.config(text="0")
                self.checkbutton1_16.deselect()

            zahlMinus8 = zahl - 8
            if zahlMinus8 >= 0:
                self.checkbutton1_8.select()
                self.label1_8.config(text="1")
                zahl = zahlMinus8
            else:
                self.label1_8.config(text="0")
                self.checkbutton1_8.deselect()

            zahlMinus4 = zahl - 4
            if zahlMinus4 >= 0:
                self.checkbutton1_4.select()
                self.label1_4.config(text="1")
                zahl = zahlMinus4
            else:
                self.label1_4.config(text="0")
                self.checkbutton1_4.deselect()

            zahlMinus2 = zahl - 2
            if zahlMinus2 >= 0:
                self.checkbutton1_2.select()
                self.label1_2.config(text="1")
                zahl = zahlMinus2
            else:
                self.label1_2.config(text="0")
                self.checkbutton1_2.deselect()

            zahlMinus1 = zahl - 1
            if zahlMinus1 >= 0:
                self.checkbutton1_1.select()
                self.label1_1.config(text="1")
            else:
                self.label1_1.config(text="0")
                self.checkbutton1_1.deselect()
        else:
            self.labelWarnung1.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

            # zweiter Teil der IP

        try:
            zahl = int(self.label2.cget("text"))
        except:
            zahl = -1
            self.labelWarnung2.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        if 0 <= zahl < 256:
            self.labelWarnung2.config(text="")

            zahlMinus128 = zahl - 128
            if zahlMinus128 >= 0:
                self.checkbutton2_128.select()
                self.label2_128.config(text="1")
                zahl = zahlMinus128
            else:
                self.label2_128.config(text="0")
                self.checkbutton2_128.deselect()

            zahlMinus64 = zahl - 64
            if zahlMinus64 >= 0:
                self.checkbutton2_64.select()
                self.label2_64.config(text="1")
                zahl = zahlMinus64
            else:
                self.label2_64.config(text="0")
                self.checkbutton2_64.deselect()

            zahlMinus32 = zahl - 32
            if zahlMinus32 >= 0:
                self.checkbutton2_32.select()
                self.label2_32.config(text="1")
                zahl = zahlMinus32
            else:
                self.label2_32.config(text="0")
                self.checkbutton2_32.deselect()

            zahlMinus16 = zahl - 16
            if zahlMinus16 >= 0:
                self.checkbutton2_16.select()
                self.label2_16.config(text="1")
                zahl = zahlMinus16
            else:
                self.label2_16.config(text="0")
                self.checkbutton2_16.deselect()

            zahlMinus8 = zahl - 8
            if zahlMinus8 >= 0:
                self.checkbutton2_8.select()
                self.label2_8.config(text="1")
                zahl = zahlMinus8
            else:
                self.label2_8.config(text="0")
                self.checkbutton2_8.deselect()

            zahlMinus4 = zahl - 4
            if zahlMinus4 >= 0:
                self.checkbutton2_4.select()
                self.label2_4.config(text="1")
                zahl = zahlMinus4
            else:
                self.label2_4.config(text="0")
                self.checkbutton2_4.deselect()

            zahlMinus2 = zahl - 2
            if zahlMinus2 >= 0:
                self.checkbutton2_2.select()
                self.label2_2.config(text="1")
                zahl = zahlMinus2
            else:
                self.label2_2.config(text="0")
                self.checkbutton2_2.deselect()

            zahlMinus1 = zahl - 1
            if zahlMinus1 >= 0:
                self.checkbutton2_1.select()
                self.label2_1.config(text="1")
            else:
                self.label2_1.config(text="0")
                self.checkbutton2_1.deselect()
        else:
            self.labelWarnung2.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        # dritter Teil der IP

        try:
            zahl = int(self.label3.cget("text"))
        except:
            zahl = -1
            self.labelWarnung3.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        if 0 <= zahl < 256:
            self.labelWarnung3.config(text="")

            zahlMinus128 = zahl - 128
            if zahlMinus128 >= 0:
                self.checkbutton3_128.select()
                self.label3_128.config(text="1")
                zahl = zahlMinus128
            else:
                self.label3_128.config(text="0")
                self.checkbutton3_128.deselect()

            zahlMinus64 = zahl - 64
            if zahlMinus64 >= 0:
                self.checkbutton3_64.select()
                self.label3_64.config(text="1")
                zahl = zahlMinus64
            else:
                self.label3_64.config(text="0")
                self.checkbutton3_64.deselect()

            zahlMinus32 = zahl - 32
            if zahlMinus32 >= 0:
                self.checkbutton3_32.select()
                self.label3_32.config(text="1")
                zahl = zahlMinus32
            else:
                self.label3_32.config(text="0")
                self.checkbutton3_32.deselect()

            zahlMinus16 = zahl - 16
            if zahlMinus16 >= 0:
                self.checkbutton3_16.select()
                self.label3_16.config(text="1")
                zahl = zahlMinus16
            else:
                self.label3_16.config(text="0")
                self.checkbutton3_16.deselect()

            zahlMinus8 = zahl - 8
            if zahlMinus8 >= 0:
                self.checkbutton3_8.select()
                self.label3_8.config(text="1")
                zahl = zahlMinus8
            else:
                self.label3_8.config(text="0")
                self.checkbutton3_8.deselect()

            zahlMinus4 = zahl - 4
            if zahlMinus4 >= 0:
                self.checkbutton3_4.select()
                self.label3_4.config(text="1")
                zahl = zahlMinus4
            else:
                self.label3_4.config(text="0")
                self.checkbutton3_4.deselect()

            zahlMinus2 = zahl - 2
            if zahlMinus2 >= 0:
                self.checkbutton3_2.select()
                self.label3_2.config(text="1")
                zahl = zahlMinus2
            else:
                self.label3_2.config(text="0")
                self.checkbutton3_2.deselect()

            zahlMinus1 = zahl - 1
            if zahlMinus1 >= 0:
                self.checkbutton3_1.select()
                self.label3_1.config(text="1")
            else:
                self.label3_1.config(text="0")
                self.checkbutton3_1.deselect()
        else:
            self.labelWarnung3.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        # vierter Teil der IP

        try:
            zahl = int(self.label4.cget("text"))
        except:
            zahl = -1
            self.labelWarnung4.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

        if 0 <= zahl < 256:
            self.labelWarnung4.config(text="")

            zahlMinus128 = zahl - 128
            if zahlMinus128 >= 0:
                self.checkbutton4_128.select()
                self.label4_128.config(text="1")
                zahl = zahlMinus128
            else:
                self.label4_128.config(text="0")
                self.checkbutton4_128.deselect()

            zahlMinus64 = zahl - 64
            if zahlMinus64 >= 0:
                self.checkbutton4_64.select()
                self.label4_64.config(text="1")
                zahl = zahlMinus64
            else:
                self.label4_64.config(text="0")
                self.checkbutton4_64.deselect()

            zahlMinus32 = zahl - 32
            if zahlMinus32 >= 0:
                self.checkbutton4_32.select()
                self.label4_32.config(text="1")
                zahl = zahlMinus32
            else:
                self.label4_32.config(text="0")
                self.checkbutton4_32.deselect()

            zahlMinus16 = zahl - 16
            if zahlMinus16 >= 0:
                self.checkbutton4_16.select()
                self.label4_16.config(text="1")
                zahl = zahlMinus16
            else:
                self.label4_16.config(text="0")
                self.checkbutton4_16.deselect()

            zahlMinus8 = zahl - 8
            if zahlMinus8 >= 0:
                self.checkbutton4_8.select()
                self.label4_8.config(text="1")
                zahl = zahlMinus8
            else:
                self.label4_8.config(text="0")
                self.checkbutton4_8.deselect()

            zahlMinus4 = zahl - 4
            if zahlMinus4 >= 0:
                self.checkbutton4_4.select()
                self.label4_4.config(text="1")
                zahl = zahlMinus4
            else:
                self.label4_4.config(text="0")
                self.checkbutton4_4.deselect()

            zahlMinus2 = zahl - 2
            if zahlMinus2 >= 0:
                self.checkbutton4_2.select()
                self.label4_2.config(text="1")
                zahl = zahlMinus2
            else:
                self.label4_2.config(text="0")
                self.checkbutton4_2.deselect()

            zahlMinus1 = zahl - 1
            if zahlMinus1 >= 0:
                self.checkbutton4_1.select()
                self.label4_1.config(text="1")
            else:
                self.label4_1.config(text="0")
                self.checkbutton4_1.deselect()
        else:
            self.labelWarnung4.config(text="Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen!")

    def binärZuDezimal(self):

        # erster Teil der IP

        zahl = 0
        if self.var1_128.get() == 1:
            zahl = zahl + 128
            self.label1.config(text=zahl)
            self.label1_128.config(text="1")
        else:
            self.label1_128.config(text="0")

        if self.var1_64.get() == 1:
            zahl = zahl + 64
            self.label1.config(text=zahl)
            self.label1_64.config(text="1")
        else:
            self.label1_64.config(text="0")

        if self.var1_32.get() == 1:
            zahl = zahl + 32
            self.label1.config(text=zahl)
            self.label1_32.config(text="1")
        else:
            self.label1_32.config(text="0")

        if self.var1_16.get() == 1:
            zahl = zahl + 16
            self.label1.config(text=zahl)
            self.label1_16.config(text="1")
        else:
            self.label1_16.config(text="0")

        if self.var1_8.get() == 1:
            zahl = zahl + 8
            self.label1.config(text=zahl)
            self.label1_8.config(text="1")
        else:
            self.label1_8.config(text="0")

        if self.var1_4.get() == 1:
            zahl = zahl + 4
            self.label1.config(text=zahl)
            self.label1_4.config(text="1")
        else:
            self.label1_4.config(text="0")

        if self.var1_2.get() == 1:
            zahl = zahl + 2
            self.label1.config(text=zahl)
            self.label1_2.config(text="1")
        else:
            self.label1_2.config(text="0")

        if self.var1_1.get() == 1:
            zahl = zahl + 1
            self.label1.config(text=zahl)
            self.label1_1.config(text="1")
        else:
            self.label1_1.config(text="0")

        if zahl == 0:
            self.label1.config(text=zahl)

        # zweiter Teil der IP

        zahl = 0
        if self.var2_128.get() == 1:
            zahl = zahl + 128
            self.label2.config(text=zahl)
            self.label2_128.config(text="1")
        else:
            self.label2_128.config(text="0")

        if self.var2_64.get() == 1:
            zahl = zahl + 64
            self.label2.config(text=zahl)
            self.label2_64.config(text="1")
        else:
            self.label2_64.config(text="0")

        if self.var2_32.get() == 1:
            zahl = zahl + 32
            self.label2.config(text=zahl)
            self.label2_32.config(text="1")
        else:
            self.label2_32.config(text="0")

        if self.var2_16.get() == 1:
            zahl = zahl + 16
            self.label2.config(text=zahl)
            self.label2_16.config(text="1")
        else:
            self.label2_16.config(text="0")

        if self.var2_8.get() == 1:
            zahl = zahl + 8
            self.label2.config(text=zahl)
            self.label2_8.config(text="1")
        else:
            self.label2_8.config(text="0")

        if self.var2_4.get() == 1:
            zahl = zahl + 4
            self.label2.config(text=zahl)
            self.label2_4.config(text="1")
        else:
            self.label2_4.config(text="0")

        if self.var2_2.get() == 1:
            zahl = zahl + 2
            self.label2.config(text=zahl)
            self.label2_2.config(text="1")
        else:
            self.label2_2.config(text="0")

        if self.var2_1.get() == 1:
            zahl = zahl + 1
            self.label2.config(text=zahl)
            self.label2_1.config(text="1")
        else:
            self.label2_1.config(text="0")

        if zahl == 0:
            self.label2.config(text=zahl)

        # dritter Teil der IP

        zahl = 0
        if self.var3_128.get() == 1:
            zahl = zahl + 128
            self.label3.config(text=zahl)
            self.label3_128.config(text="1")
        else:
            self.label3_128.config(text="0")

        if self.var3_64.get() == 1:
            zahl = zahl + 64
            self.label3.config(text=zahl)
            self.label3_64.config(text="1")
        else:
            self.label3_64.config(text="0")

        if self.var3_32.get() == 1:
            zahl = zahl + 32
            self.label3.config(text=zahl)
            self.label3_32.config(text="1")
        else:
            self.label3_32.config(text="0")

        if self.var3_16.get() == 1:
            zahl = zahl + 16
            self.label3.config(text=zahl)
            self.label3_16.config(text="1")
        else:
            self.label3_16.config(text="0")

        if self.var3_8.get() == 1:
            zahl = zahl + 8
            self.label3.config(text=zahl)
            self.label3_8.config(text="1")
        else:
            self.label3_8.config(text="0")

        if self.var3_4.get() == 1:
            zahl = zahl + 4
            self.label3.config(text=zahl)
            self.label3_4.config(text="1")
        else:
            self.label3_4.config(text="0")

        if self.var3_2.get() == 1:
            zahl = zahl + 2
            self.label3.config(text=zahl)
            self.label3_2.config(text="1")
        else:
            self.label3_2.config(text="0")

        if self.var3_1.get() == 1:
            zahl = zahl + 1
            self.label3.config(text=zahl)
            self.label3_1.config(text="1")
        else:
            self.label3_1.config(text="0")

        if zahl == 0:
            self.label3.config(text=zahl)

        # vierter Teil der IP

        zahl = 0
        if self.var4_128.get() == 1:
            zahl = zahl + 128
            self.label4.config(text=zahl)
            self.label4_128.config(text="1")
        else:
            self.label4_128.config(text="0")

        if self.var4_64.get() == 1:
            zahl = zahl + 64
            self.label4.config(text=zahl)
            self.label4_64.config(text="1")
        else:
            self.label4_64.config(text="0")

        if self.var4_32.get() == 1:
            zahl = zahl + 32
            self.label4.config(text=zahl)
            self.label4_32.config(text="1")
        else:
            self.label4_32.config(text="0")

        if self.var4_16.get() == 1:
            zahl = zahl + 16
            self.label4.config(text=zahl)
            self.label4_16.config(text="1")
        else:
            self.label4_16.config(text="0")

        if self.var4_8.get() == 1:
            zahl = zahl + 8
            self.label4.config(text=zahl)
            self.label4_8.config(text="1")
        else:
            self.label4_8.config(text="0")

        if self.var4_4.get() == 1:
            zahl = zahl + 4
            self.label4.config(text=zahl)
            self.label4_4.config(text="1")
        else:
            self.label4_4.config(text="0")

        if self.var4_2.get() == 1:
            zahl = zahl + 2
            self.label4.config(text=zahl)
            self.label4_2.config(text="1")
        else:
            self.label4_2.config(text="0")

        if self.var4_1.get() == 1:
            zahl = zahl + 1
            self.label4.config(text=zahl)
            self.label4_1.config(text="1")
        else:
            self.label4_1.config(text="0")

        if zahl == 0:
            self.label4.config(text=zahl)

        self.dezimalZuBinär()

    def ipSplit(self):

        ip = self.entry01.get()
        ipListe = ip.split(".")
        try:
            self.ersterTeil = ipListe[0]
            self.zweiterTeil = ipListe[1]
            self.dritterTeil = ipListe[2]
            self.vierterTeil = ipListe[3]
        except:
            print("Keine gültige IP! IPs zwischen 0 und 255 pro Stelle eintragen! zB: 192.168.0.1")

        self.label1.config(text=self.ersterTeil)
        self.label2.config(text=self.zweiterTeil)
        self.label3.config(text=self.dritterTeil)
        self.label4.config(text=self.vierterTeil)

        self.cidrSuffixZuNetzwerkmaske()
        self.dezimalZuBinär()

    def binärZuIP(self):

        self.binärZuDezimal()
        ipStr = str(self.label1.cget("text")) + "." + str(self.label2.cget("text")) + "." + str(
            self.label3.cget("text")) + "." + str(self.label4.cget("text"))
        self.v1.set(ipStr)

        self.ipSplit()
        self.netzadresseBerechnen()

    def cidrSuffixZuNetzwerkmaske(self):
        try:
            cidrSuffix = int(self.v2.get())
        except:
            cidrSuffix = ""
            self.v3.set("CIDR 0 bis 32 erlaubt")
        try:
            if cidrSuffix == 32:
                self.v3.set("255.255.255.255")
            elif cidrSuffix == 31:
                self.v3.set("255.255.255.254")
            elif cidrSuffix == 30:
                self.v3.set("255.255.255.252")
            elif cidrSuffix == 29:
                self.v3.set("255.255.255.248")
            elif cidrSuffix == 28:
                self.v3.set("255.255.255.240")
            elif cidrSuffix == 27:
                self.v3.set("255.255.255.224")
            elif cidrSuffix == 26:
                self.v3.set("255.255.255.192")
            elif cidrSuffix == 25:
                self.v3.set("255.255.255.128")
            elif cidrSuffix == 24:
                self.v3.set("255.255.255.0")
            elif cidrSuffix == 23:
                self.v3.set("255.255.254.0")
            elif cidrSuffix == 22:
                self.v3.set("255.255.252.0")
            elif cidrSuffix == 21:
                self.v3.set("255.255.248.0")
            elif cidrSuffix == 20:
                self.v3.set("255.255.240.0")
            elif cidrSuffix == 19:
                self.v3.set("255.255.224.0")
            elif cidrSuffix == 18:
                self.v3.set("255.255.192.0")
            elif cidrSuffix == 17:
                self.v3.set("255.255.128.0")
            elif cidrSuffix == 16:
                self.v3.set("255.255.0.0")
            elif cidrSuffix == 15:
                self.v3.set("255.254.0.0")
            elif cidrSuffix == 14:
                self.v3.set("255.252.0.0")
            elif cidrSuffix == 13:
                self.v3.set("255.248.0.0")
            elif cidrSuffix == 12:
                self.v3.set("255.240.0.0")
            elif cidrSuffix == 11:
                self.v3.set("255.224.0.0")
            elif cidrSuffix == 10:
                self.v3.set("255.192.0.0")
            elif cidrSuffix == 9:
                self.v3.set("255.128.0.0")
            elif cidrSuffix == 8:
                self.v3.set("255.0.0.0")
            elif cidrSuffix == 7:
                self.v3.set("254.0.0.0")
            elif cidrSuffix == 6:
                self.v3.set("252.0.0.0")
            elif cidrSuffix == 5:
                self.v3.set("248.0.0.0")
            elif cidrSuffix == 4:
                self.v3.set("240.0.0.0")
            elif cidrSuffix == 3:
                self.v3.set("224.0.0.0")
            elif cidrSuffix == 2:
                self.v3.set("192.255.0.0")
            elif cidrSuffix == 1:
                self.v3.set("128.0.0.0")
            elif cidrSuffix == 0:
                self.v3.set("0.0.0.0")
            elif cidrSuffix > 32:
                self.v3.set("CIDR zu hoch")
            elif cidrSuffix < 0:
                self.v3.set("CIDR zu klein")
        except:
            self.v3.set("CIDR 0 bis 32 erlaubt")

        self.anzahlHostAusCIDR()

    def netzwerkmaskeZuCIDRSuffix(self):

        netzwerkmaske = self.v3.get()
        try:
            if netzwerkmaske == "255.255.255.255":
                self.v2.set(32)
            elif netzwerkmaske == "255.255.255.254":
                self.v2.set(31)
            elif netzwerkmaske == "255.255.255.252":
                self.v2.set(30)
            elif netzwerkmaske == "255.255.255.248":
                self.v2.set(29)
            elif netzwerkmaske == "255.255.255.240":
                self.v2.set(28)
            elif netzwerkmaske == "255.255.255.224":
                self.v2.set(27)
            elif netzwerkmaske == "255.255.255.192":
                self.v2.set(26)
            elif netzwerkmaske == "255.255.255.128":
                self.v2.set(25)
            elif netzwerkmaske == "255.255.255.0":
                self.v2.set(24)
            elif netzwerkmaske == "255.255.254.0":
                self.v2.set(23)
            elif netzwerkmaske == "255.255.252.0":
                self.v2.set(22)
            elif netzwerkmaske == "255.255.248.0":
                self.v2.set(21)
            elif netzwerkmaske == "255.255.240.0":
                self.v2.set(20)
            elif netzwerkmaske == "255.255.224.0":
                self.v2.set(19)
            elif netzwerkmaske == "255.255.192.0":
                self.v2.set(18)
            elif netzwerkmaske == "255.255.128.0":
                self.v2.set(17)
            elif netzwerkmaske == "255.255.0.0":
                self.v2.set(16)
            elif netzwerkmaske == "255.254.0.0":
                self.v2.set(15)
            elif netzwerkmaske == "255.252.0.0":
                self.v2.set(14)
            elif netzwerkmaske == "255.248.0.0":
                self.v2.set(13)
            elif netzwerkmaske == "255.240.0.0":
                self.v2.set(12)
            elif netzwerkmaske == "255.224.0.0":
                self.v2.set(11)
            elif netzwerkmaske == "255.192.0.0":
                self.v2.set(10)
            elif netzwerkmaske == "255.128.0.0":
                self.v2.set(9)
            elif netzwerkmaske == "255.0.0.0":
                self.v2.set(8)
            elif netzwerkmaske == "254.0.0.0":
                self.v2.set(7)
            elif netzwerkmaske == "252.0.0.0":
                self.v2.set(6)
            elif netzwerkmaske == "248.0.0.0":
                self.v2.set(5)
            elif netzwerkmaske == "240.0.0.0":
                self.v2.set(4)
            elif netzwerkmaske == "224.0.0.0":
                self.v2.set(3)
            elif netzwerkmaske == "192.255.0.0":
                self.v2.set(2)
            elif netzwerkmaske == "128.0.0.0":
                self.v2.set(1)
            elif netzwerkmaske == "0.0.0.0":
                self.v2.set(0)
            else:
                self.v2.set("Falsche Netzwerkmaske")
        except:
            self.v2.set("Falsche Netzwerkmaske")

        self.netzadresseBerechnen()

    def anzahlHostAusCIDR(self):
        try:
            cidrSuffix = int(self.v2.get())
        except:
            cidrSuffix = ""
        try:
            anzahlHost = 2 ** (32 - cidrSuffix) - 2
            if anzahlHost < 0:
                anzahlHost = 0
                self.labelAnzahlHosts.config(text=anzahlHost)
            elif cidrSuffix < 0:
                self.labelAnzahlHosts.config(text="CIDR zu klein")
            else:
                self.labelAnzahlHosts.config(text=anzahlHost)
        except:
            self.labelAnzahlHosts.config(text="CIDR 0 bis 32 erlaubt")

        self.netzadresseBerechnen()

    def netzwerkmaskeSplit(self):

        netzwerkmaske = self.v3.get()

        netzwerkmaskeListe = netzwerkmaske.split(".")

        self.netzwerkmaskeErsterTeil = netzwerkmaskeListe[0]
        self.netzwerkmaskeZweiterTeil = netzwerkmaskeListe[1]
        self.netzwerkmaskeDritterTeil = netzwerkmaskeListe[2]
        self.netzwerkmaskeVierterTeil = netzwerkmaskeListe[3]

    def netzadresseBerechnen(self):

        self.netzwerkmaskeSplit()

        netzwerkmaskeErsterTeilInt = int(bin(int(self.netzwerkmaskeErsterTeil)), 2)
        netzwerkmaskeZweiterTeilInt = int(bin(int(self.netzwerkmaskeZweiterTeil)), 2)
        netzwerkmaskeDritterTeilInt = int(bin(int(self.netzwerkmaskeDritterTeil)), 2)
        netzwerkmaskeVierterTeilInt = int(bin(int(self.netzwerkmaskeVierterTeil)), 2)

        ersterTeilInt = int(bin(int(self.ersterTeil)), 2)
        zweiterTeilInt = int(bin(int(self.zweiterTeil)), 2)
        dritterTeilInt = int(bin(int(self.dritterTeil)), 2)
        vierterTeilInt = int(bin(int(self.vierterTeil)), 2)

        netzwerkAdresseErsterTeilBinär = bin(ersterTeilInt & netzwerkmaskeErsterTeilInt)
        netzwerkAdresseErsterTeil = int(netzwerkAdresseErsterTeilBinär, 2)

        netzwerkAdresseZweiterTeilBinär = bin(zweiterTeilInt & netzwerkmaskeZweiterTeilInt)
        netzwerkAdresseZweiterTeil = int(netzwerkAdresseZweiterTeilBinär, 2)

        netzwerkAdresseDritterTeilBinär = bin(dritterTeilInt & netzwerkmaskeDritterTeilInt)
        netzwerkAdresseDritterTeil = int(netzwerkAdresseDritterTeilBinär, 2)

        netzwerkAdresseVierterTeilBinär = bin(vierterTeilInt & netzwerkmaskeVierterTeilInt)
        netzwerkAdresseVierterTeil = int(netzwerkAdresseVierterTeilBinär, 2)

        netzwerkAdresse = f"{netzwerkAdresseErsterTeil}.{netzwerkAdresseZweiterTeil}.{netzwerkAdresseDritterTeil}.{netzwerkAdresseVierterTeil}"

        self.labelNetzadresse.config(text=netzwerkAdresse)

        self.broadcastAdresseBerechnen()

    def broadcastAdresseBerechnen(self):

        # nutzen des IPAddress Moduls

        IP = self.v1.get()
        MASK = self.v3.get()

        # host = ipaddress.IPv4Address(IP)
        net = ipaddress.IPv4Network(IP + '/' + MASK, False)
        # print('IP:', IP)
        # print('Mask:', MASK)
        # print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
        # print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
        self.labelBroadcast.config(text=net.broadcast_address)



if __name__ == "__main__":
    mw = TkinterFenster()
    mw.title("IP Rechner")
    mw.configure(background=mw.background)
    mw.resizable(width=False, height=False)
    mw.mainloop()