from tkinter import *
from tkinter import font as tkFont

class UI_MainWindow:
    def setup(self):
        self.font01 = tkFont.Font(family="Arial", size=10)
        self.background = "lightgrey"
        self.foreground = "black"

        self.colorNormal = "black"
        self.colorRed = "red"
        self.labelSorte = "ridge"
        self.widthCheckbuttons = 5
        self.widthLabels = 10

        Label(self, text="IP-Adresse:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=0, column=0, sticky=N + E + S + W)

        Label(self, text="CIDR-Suffix:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=2, column=0, sticky=N + E + S + W)

        Label(self, text="Netzwerkmaske:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=4, column=0, sticky=N + E + S + W)

        Label(self, text="Anzahl Hosts:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=6, column=0, sticky=N + E + S + W)

        Label(self, text="Netzadresse:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=8, column=0, sticky=N + E + S + W)

        Label(self, text="Broadcast-Adresse:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=10, column=0, sticky=N + E + S + W)

        Label(self, text="Dezimal:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=0, column=1, sticky=N + E + S + W)

        Label(self, text="Dezimal:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=3, column=1, sticky=N + E + S + W)

        Label(self, text="Dezimal:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=6, column=1, sticky=N + E + S + W)

        Label(self, text="Dezimal:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=9, column=1, sticky=N + E + S + W)

        Label(self, text="Binär:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=1, column=1, sticky=N + E + S + W)

        Label(self, text="Binär:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=4, column=1, sticky=N + E + S + W)

        Label(self, text="Binär:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=7, column=1, sticky=N + E + S + W)

        Label(self, text="Binär:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=10, column=1, sticky=N + E + S + W)

        Label(self, text="Potenzen:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=2, column=1, sticky=N + E + S + W)

        Label(self, text="Potenzen:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=5, column=1, sticky=N + E + S + W)

        Label(self, text="Potenzen:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=8, column=1, sticky=N + E + S + W)

        Label(self, text="Potenzen:", relief=self.labelSorte, bg=self.background, fg=self.foreground,
              font=self.font01, width=self.widthLabels).grid(row=11, column=1, sticky=N + E + S + W)

        self.v1 = StringVar(self, value="192.168.0.1")
        self.entry01 = Entry(self, textvariable=self.v1, font=self.font01)
        self.entry01.grid(row=1, column=0, sticky=N + E + S + W)

        self.v2 = StringVar(self, value="24")
        self.entry02 = Entry(self, textvariable=self.v2, font=self.font01)
        self.entry02.grid(row=3, column=0, sticky=N + E + S + W)

        self.v3 = StringVar(self, value="255.255.255.0")
        self.entry03 = Entry(self, textvariable=self.v3, font=self.font01)
        self.entry03.grid(row=5, column=0, sticky=N + E + S + W)

        self.label1 = Label(self, text="192", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                            font=self.font01, width=self.widthCheckbuttons)
        self.label1.grid(row=0, column=2, sticky=N + E + S + W)

        self.label1_128 = Label(self, text="0", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                                font=self.font01, width=self.widthCheckbuttons)
        self.label1_128.grid(row=1, column=2, sticky=N + E + S + W)

        self.label1_64 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label1_64.grid(row=1, column=3, sticky=N + E + S + W)

        self.label1_32 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label1_32.grid(row=1, column=4, sticky=N + E + S + W)

        self.label1_16 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label1_16.grid(row=1, column=5, sticky=N + E + S + W)

        self.label1_8 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label1_8.grid(row=1, column=6, sticky=N + E + S + W)

        self.label1_4 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label1_4.grid(row=1, column=7, sticky=N + E + S + W)

        self.label1_2 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label1_2.grid(row=1, column=8, sticky=N + E + S + W)

        self.label1_1 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label1_1.grid(row=1, column=9, sticky=N + E + S + W)

        self.var1_128 = IntVar()
        self.checkbutton1_128 = Checkbutton(self, text="128", relief=self.labelSorte, bg=self.background,
                                            fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                            variable=self.var1_128, command=self.binärZuIP)
        self.checkbutton1_128.grid(row=2, column=2, sticky=N + E + S + W)

        self.var1_64 = IntVar()
        self.checkbutton1_64 = Checkbutton(self, text="64", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var1_64, command=self.binärZuIP)
        self.checkbutton1_64.grid(row=2, column=3, sticky=N + E + S + W)

        self.var1_32 = IntVar()
        self.checkbutton1_32 = Checkbutton(self, text="32", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var1_32, command=self.binärZuIP)
        self.checkbutton1_32.grid(row=2, column=4, sticky=N + E + S + W)

        self.var1_16 = IntVar()
        self.checkbutton1_16 = Checkbutton(self, text="16", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var1_16, command=self.binärZuIP)
        self.checkbutton1_16.grid(row=2, column=5, sticky=N + E + S + W)

        self.var1_8 = IntVar()
        self.checkbutton1_8 = Checkbutton(self, text="8", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var1_8, command=self.binärZuIP)
        self.checkbutton1_8.grid(row=2, column=6, sticky=N + E + S + W)

        self.var1_4 = IntVar()
        self.checkbutton1_4 = Checkbutton(self, text="4", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var1_4, command=self.binärZuIP)
        self.checkbutton1_4.grid(row=2, column=7, sticky=N + E + S + W)

        self.var1_2 = IntVar()
        self.checkbutton1_2 = Checkbutton(self, text="2", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var1_2, command=self.binärZuIP)
        self.checkbutton1_2.grid(row=2, column=8, sticky=N + E + S + W)

        self.var1_1 = IntVar()
        self.checkbutton1_1 = Checkbutton(self, text="1", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var1_1, command=self.binärZuIP)
        self.checkbutton1_1.grid(row=2, column=9, sticky=N + E + S + W)

        self.label2 = Label(self, text="246", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                            font=self.font01, width=self.widthCheckbuttons)
        self.label2.grid(row=3, column=2, sticky=N + E + S + W)

        self.label2_128 = Label(self, text="0", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                                font=self.font01, width=self.widthCheckbuttons)
        self.label2_128.grid(row=4, column=2, sticky=N + E + S + W)

        self.label2_64 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label2_64.grid(row=4, column=3, sticky=N + E + S + W)

        self.label2_32 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label2_32.grid(row=4, column=4, sticky=N + E + S + W)

        self.label2_16 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label2_16.grid(row=4, column=5, sticky=N + E + S + W)

        self.label2_8 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label2_8.grid(row=4, column=6, sticky=N + E + S + W)

        self.label2_4 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label2_4.grid(row=4, column=7, sticky=N + E + S + W)

        self.label2_2 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label2_2.grid(row=4, column=8, sticky=N + E + S + W)

        self.label2_1 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label2_1.grid(row=4, column=9, sticky=N + E + S + W)

        self.var2_128 = IntVar()
        self.checkbutton2_128 = Checkbutton(self, text="128", relief=self.labelSorte, bg=self.background,
                                            fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                            variable=self.var2_128, command=self.binärZuIP)
        self.checkbutton2_128.grid(row=5, column=2, sticky=N + E + S + W)

        self.var2_64 = IntVar()
        self.checkbutton2_64 = Checkbutton(self, text="64", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var2_64, command=self.binärZuIP)
        self.checkbutton2_64.grid(row=5, column=3, sticky=N + E + S + W)

        self.var2_32 = IntVar()
        self.checkbutton2_32 = Checkbutton(self, text="32", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var2_32, command=self.binärZuIP)
        self.checkbutton2_32.grid(row=5, column=4, sticky=N + E + S + W)

        self.var2_16 = IntVar()
        self.checkbutton2_16 = Checkbutton(self, text="16", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var2_16, command=self.binärZuIP)
        self.checkbutton2_16.grid(row=5, column=5, sticky=N + E + S + W)

        self.var2_8 = IntVar()
        self.checkbutton2_8 = Checkbutton(self, text="8", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var2_8, command=self.binärZuIP)
        self.checkbutton2_8.grid(row=5, column=6, sticky=N + E + S + W)

        self.var2_4 = IntVar()
        self.checkbutton2_4 = Checkbutton(self, text="4", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var2_4, command=self.binärZuIP)
        self.checkbutton2_4.grid(row=5, column=7, sticky=N + E + S + W)

        self.var2_2 = IntVar()
        self.checkbutton2_2 = Checkbutton(self, text="2", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var2_2, command=self.binärZuIP)
        self.checkbutton2_2.grid(row=5, column=8, sticky=N + E + S + W)

        self.var2_1 = IntVar()
        self.checkbutton2_1 = Checkbutton(self, text="1", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var2_1, command=self.binärZuIP)
        self.checkbutton2_1.grid(row=5, column=9, sticky=N + E + S + W)

        # dritter Teil der IP

        self.label3 = Label(self, text="0", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                            font=self.font01, width=self.widthCheckbuttons)
        self.label3.grid(row=6, column=2, sticky=N + E + S + W)

        self.label3_128 = Label(self, text="0", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                                font=self.font01, width=self.widthCheckbuttons)
        self.label3_128.grid(row=7, column=2, sticky=N + E + S + W)

        self.label3_64 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label3_64.grid(row=7, column=3, sticky=N + E + S + W)

        self.label3_32 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label3_32.grid(row=7, column=4, sticky=N + E + S + W)

        self.label3_16 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label3_16.grid(row=7, column=5, sticky=N + E + S + W)

        self.label3_8 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label3_8.grid(row=7, column=6, sticky=N + E + S + W)

        self.label3_4 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label3_4.grid(row=7, column=7, sticky=N + E + S + W)

        self.label3_2 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label3_2.grid(row=7, column=8, sticky=N + E + S + W)

        self.label3_1 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label3_1.grid(row=7, column=9, sticky=N + E + S + W)

        self.var3_128 = IntVar()
        self.checkbutton3_128 = Checkbutton(self, text="128", relief=self.labelSorte, bg=self.background,
                                            fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                            variable=self.var3_128, command=self.binärZuIP)
        self.checkbutton3_128.grid(row=8, column=2, sticky=N + E + S + W)

        self.var3_64 = IntVar()
        self.checkbutton3_64 = Checkbutton(self, text="64", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var3_64, command=self.binärZuIP)
        self.checkbutton3_64.grid(row=8, column=3, sticky=N + E + S + W)

        self.var3_32 = IntVar()
        self.checkbutton3_32 = Checkbutton(self, text="32", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var3_32, command=self.binärZuIP)
        self.checkbutton3_32.grid(row=8, column=4, sticky=N + E + S + W)

        self.var3_16 = IntVar()
        self.checkbutton3_16 = Checkbutton(self, text="16", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var3_16, command=self.binärZuIP)
        self.checkbutton3_16.grid(row=8, column=5, sticky=N + E + S + W)

        self.var3_8 = IntVar()
        self.checkbutton3_8 = Checkbutton(self, text="8", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var3_8, command=self.binärZuIP)
        self.checkbutton3_8.grid(row=8, column=6, sticky=N + E + S + W)

        self.var3_4 = IntVar()
        self.checkbutton3_4 = Checkbutton(self, text="4", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var3_4, command=self.binärZuIP)
        self.checkbutton3_4.grid(row=8, column=7, sticky=N + E + S + W)

        self.var3_2 = IntVar()
        self.checkbutton3_2 = Checkbutton(self, text="2", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var3_2, command=self.binärZuIP)
        self.checkbutton3_2.grid(row=8, column=8, sticky=N + E + S + W)

        self.var3_1 = IntVar()
        self.checkbutton3_1 = Checkbutton(self, text="1", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var3_1, command=self.binärZuIP)
        self.checkbutton3_1.grid(row=8, column=9, sticky=N + E + S + W)

        # vierter Teil der IP

        self.label4 = Label(self, text="1", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                            font=self.font01, width=self.widthCheckbuttons)
        self.label4.grid(row=9, column=2, sticky=N + E + S + W)

        self.label4_128 = Label(self, text="0", relief=self.labelSorte, bg=self.background, fg=self.foreground,
                                font=self.font01, width=self.widthCheckbuttons)
        self.label4_128.grid(row=10, column=2, sticky=N + E + S + W)

        self.label4_64 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label4_64.grid(row=10, column=3, sticky=N + E + S + W)

        self.label4_32 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label4_32.grid(row=10, column=4, sticky=N + E + S + W)

        self.label4_16 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                               fg=self.foreground,
                               font=self.font01, width=self.widthCheckbuttons)
        self.label4_16.grid(row=10, column=5, sticky=N + E + S + W)

        self.label4_8 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label4_8.grid(row=10, column=6, sticky=N + E + S + W)

        self.label4_4 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label4_4.grid(row=10, column=7, sticky=N + E + S + W)

        self.label4_2 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label4_2.grid(row=10, column=8, sticky=N + E + S + W)

        self.label4_1 = Label(self, text="0", relief=self.labelSorte, bg=self.background,
                              fg=self.foreground,
                              font=self.font01, width=self.widthCheckbuttons)
        self.label4_1.grid(row=10, column=9, sticky=N + E + S + W)

        self.var4_128 = IntVar()
        self.checkbutton4_128 = Checkbutton(self, text="128", relief=self.labelSorte, bg=self.background,
                                            fg=self.foreground,
                                            font=self.font01, width=self.widthCheckbuttons, variable=self.var4_128,
                                            command=self.binärZuIP)
        self.checkbutton4_128.grid(row=11, column=2, sticky=N + E + S + W)

        self.var4_64 = IntVar()
        self.checkbutton4_64 = Checkbutton(self, text="64", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var4_64,
                                           command=self.binärZuIP)
        self.checkbutton4_64.grid(row=11, column=3, sticky=N + E + S + W)

        self.var4_32 = IntVar()
        self.checkbutton4_32 = Checkbutton(self, text="32", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var4_32,
                                           command=self.binärZuIP)
        self.checkbutton4_32.grid(row=11, column=4, sticky=N + E + S + W)

        self.var4_16 = IntVar()
        self.checkbutton4_16 = Checkbutton(self, text="16", relief=self.labelSorte, bg=self.background,
                                           fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                           variable=self.var4_16,
                                           command=self.binärZuIP)
        self.checkbutton4_16.grid(row=11, column=5, sticky=N + E + S + W)

        self.var4_8 = IntVar()
        self.checkbutton4_8 = Checkbutton(self, text="8", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var4_8,
                                          command=self.binärZuIP)
        self.checkbutton4_8.grid(row=11, column=6, sticky=N + E + S + W)

        self.var4_4 = IntVar()
        self.checkbutton4_4 = Checkbutton(self, text="4", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var4_4,
                                          command=self.binärZuIP)
        self.checkbutton4_4.grid(row=11, column=7, sticky=N + E + S + W)

        self.var4_2 = IntVar()
        self.checkbutton4_2 = Checkbutton(self, text="2", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var4_2,
                                          command=self.binärZuIP)
        self.checkbutton4_2.grid(row=11, column=8, sticky=N + E + S + W)

        self.var4_1 = IntVar()
        self.checkbutton4_1 = Checkbutton(self, text="1", relief=self.labelSorte, bg=self.background,
                                          fg=self.foreground, font=self.font01, width=self.widthCheckbuttons,
                                          variable=self.var4_1,
                                          command=self.binärZuIP)
        self.checkbutton4_1.grid(row=11, column=9, sticky=N + E + S + W)

        # self.button01 = Button(self, text="IP übernehmen",
        #                       command=self.ipSplit,
        #                      bg=self.background, fg=self.foreground, font=self.font01)
        # self.button01.grid(row=2, column=0, sticky=N + E + S + W)

        # Warnungs Labels erstellen

        self.labelWarnung1 = Label(self, text="", relief=self.labelSorte, bg=self.background, fg=self.colorRed,
                                   font=self.font01, width=self.widthLabels)
        self.labelWarnung1.grid(row=0, column=3, columnspan=7, sticky=N + E + S + W)

        self.labelWarnung2 = Label(self, text="", relief=self.labelSorte, bg=self.background, fg=self.colorRed,
                                   font=self.font01, width=self.widthLabels)
        self.labelWarnung2.grid(row=3, column=3, columnspan=7, sticky=N + E + S + W)

        self.labelWarnung3 = Label(self, text="", relief=self.labelSorte, bg=self.background, fg=self.colorRed,
                                   font=self.font01, width=self.widthLabels)
        self.labelWarnung3.grid(row=6, column=3, columnspan=7, sticky=N + E + S + W)

        self.labelWarnung4 = Label(self, text="", relief=self.labelSorte, bg=self.background, fg=self.colorRed,
                                   font=self.font01, width=self.widthLabels)
        self.labelWarnung4.grid(row=9, column=3, columnspan=7, sticky=N + E + S + W)

        self.labelAnzahlHosts = Label(self, text="254", relief=self.labelSorte, bg=self.background,
                                      fg=self.foreground,
                                      font=self.font01, width=self.widthLabels)
        self.labelAnzahlHosts.grid(row=7, column=0, sticky=N + E + S + W)

        self.labelNetzadresse = Label(self, text="192.168.0.0", relief=self.labelSorte, bg=self.background,
                                      fg=self.foreground,
                                      font=self.font01, width=self.widthLabels)
        self.labelNetzadresse.grid(row=9, column=0, sticky=N + E + S + W)

        self.labelBroadcast = Label(self, text="192.168.0.255", relief=self.labelSorte, bg=self.background,
                                    fg=self.foreground,
                                    font=self.font01, width=self.widthLabels)
        self.labelBroadcast.grid(row=11, column=0, sticky=N + E + S + W)