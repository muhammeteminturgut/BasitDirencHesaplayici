from tkinter import *
from tkinter import ttk
import tkinter.messagebox
class DirencHesaplayici:
    def __init__(self):
        self.pencere=Tk()
        self.pencere.resizable(False, False)
        self.pencere.title("Basit Direnç Hesaplayıcı | Muhammet Emin TURGUT")

        # <Grup1>
        self.grup1 = ttk.LabelFrame(self.pencere, text=" Direnç Bant Sayısı: ")
        self.grup1.grid(row=0,column=0,padx=10, pady=10, ipadx=5, ipady=5,columnspan=2,sticky="we")
        self.bantSecim=IntVar()
        self.bantSecim.set(5)
        self.dortBant_Radio=ttk.Radiobutton(self.grup1,text="4 Bantlı Direnç",value=4,variable=self.bantSecim,width=36).grid(row=0,column=0)
        self.besBant_Radio =ttk.Radiobutton(self.grup1, text="5 Bantlı Direnç", value=5,variable=self.bantSecim,width=36).grid(row=0,column=1)
        self.Button = ttk.Button(self.grup1,text="Seç",command=self.direncBantAyar).grid(row=0,column=3)
        # </Grup1>

        # <Grup2>
        self.grup2 = ttk.LabelFrame(self.pencere, text=" Direnç: ")
        self.grup2.grid(row=1,column=0,padx=10, pady=10, ipadx=5, ipady=5,columnspan=2,sticky="we")
        self.kanvas = Canvas(self.grup2, width=550, height=100)
        self.kanvas.pack()
        self.kablo = self.kanvas.create_rectangle(0, 50, 1000, 50, tags="kablo")
        self.direnc = self.kanvas.create_rectangle(160, 20, 385, 80, tags="direnc", outline='#D1A969',fill="#D1A969")
        self.sol_direnc = self.kanvas.create_rectangle(160, 10, 190, 90, tags="sol_direnc", outline='#D1A969', fill="#D1A969")
        self.sag_direnc = self.kanvas.create_rectangle(355, 10, 385, 90, tags="sag_direnc", outline='#D1A969', fill="#D1A969")
        # </Grup2>

        # <Grup3>
        self.grup3 = ttk.LabelFrame(self.pencere, text=" Bant Renkleri: ")
        self.grup3.grid(row=2,column=0,padx=10, pady=10, ipadx=5, ipady=5,columnspan=2,sticky="we")
        self.lbl_Bas1 = Label(self.grup3,text="1. Basamak",width=15)
        self.lbl_Bas2 = Label(self.grup3, text="2. Basamak",width=15)
        self.lbl_Bas3 = Label(self.grup3, text="3. Basamak",width=15)
        self.lbl_Carp = Label(self.grup3, text="Çarpan",width=15)
        self.lbl_Tol = Label(self.grup3, text="Tolerans",width=15)
        self.lbl_Bas1.grid(row=0,column=0)
        self.lbl_Bas2.grid(row=0, column=1)
        self.lbl_Bas3.grid(row=0, column=2)
        self.lbl_Carp.grid(row=0, column=3)
        self.lbl_Tol.grid(row=0, column=4)

        self.combo_Bas1 = ttk.Combobox(self.grup3,state='readonly',
                                       values=["Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor",
                                               "Gri", "Beyaz"], width=12)
        self.combo_Bas2 = ttk.Combobox(self.grup3,state='readonly',
                                       values=["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi",
                                               "Mor", "Gri", "Beyaz"], width=12)
        self.combo_Bas3 = ttk.Combobox(self.grup3,state='readonly',
                                       values=["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi",
                                               "Mor", "Gri", "Beyaz"], width=12)
        self.combo_Carp = ttk.Combobox(self.grup3,state='readonly',
                                       values=["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi",
                                               "Mor", "Gri", "Beyaz", "Altın", "Gümüş"], width=12)
        self.combo_Tol = ttk.Combobox(self.grup3,state='readonly',
                                       values=["Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi",
                                               "Mor", "Gri","Altın", "Gümüş"], width=12)
        self.combo_Bas1.grid(row=1, column=0)
        self.combo_Bas2.grid(row=1, column=1)
        self.combo_Bas3.grid(row=1, column=2)
        self.combo_Carp.grid(row=1, column=3)
        self.combo_Tol.grid(row=1, column=4)
        # </Grup3>

        # <AyarMenüsü>
        self.renkUygula=ttk.Button(self.pencere,text="Ayarları Uygula",width=44,command=self.direncHesaplayici).grid(row=3, column=0,pady=2)
        self.renkTemizle = ttk.Button(self.pencere, text="Renkleri Temizle", width=45,command=self.kanvasTemizle).grid(row=3, column=1,pady=2)
        self.separator = ttk.Separator(self.pencere, orient="horizontal").grid(row=4, column=0, sticky="we",columnspan=2,pady=4,padx=10)
        self.netDeger=StringVar()
        self.aralik=StringVar()
        self.lblNetDeger = ttk.Label(self.pencere,text="Net Direnç Değeri: ").grid(row=5, column=0,pady=4)
        self.lblNetDegerGoster = ttk.Label(self.pencere, textvariable=self.netDeger, foreground="red").grid(row=5, column=1, pady=4)
        self.lblNetDeger = ttk.Label(self.pencere,text="Minimum ve Maksimum Değer Aralığı: ").grid(row=6, column=0,pady=4)
        self.lblNetDegerGoster = ttk.Label(self.pencere, textvariable=self.aralik, foreground="red").grid(row=6, column=1, pady=4)
        # </AyarMenüsü>

        #<Tkinter Pencere Ortalayıcı>
        self.pencere.attributes('-alpha', 0.0)
        self.pencere.update_idletasks()
        width = self.pencere.winfo_width()
        frm_width = self.pencere.winfo_rootx() - self.pencere.winfo_x()
        win_width = width + 2 * frm_width
        height = self.pencere.winfo_height()
        titlebar_height = self.pencere.winfo_rooty() - self.pencere.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.pencere.winfo_screenwidth() // 2 - win_width // 2
        y = self.pencere.winfo_screenheight() // 2 - win_height // 2
        self.pencere.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.pencere.deiconify()
        self.pencere.attributes('-alpha', 1.0)
        #</Tkinter Pencere Ortalayıcı>
        self.pencere.mainloop()

    def direncBantAyar(self):
        if self.bantSecim.get() == 4:
            self.lbl_Bas3.configure(state='disabled')
            self.combo_Bas3.configure(state='disabled')
        elif self.bantSecim.get() == 5:
            self.lbl_Bas3.configure(state='normal')
            self.combo_Bas3.configure(state='readonly')

    def direncHesaplayici(self):
        sozlukSayi = {"Siyah": 0, "Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 5, "Mavi": 6,
                      "Mor": 7, "Gri": 8, "Beyaz": 9, "Altın": -1, "Gümüş": -2}
        sozlukTolerans = {"Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 0.5, "Mavi": 0.25,
                      "Mor": 0.10, "Gri": 0.05,"Altın": 5, "Gümüş": 10}
        try:
            if self.bantSecim.get() == 4:
                self.netSayi=int(str(sozlukSayi[self.combo_Bas1.get()])+str(sozlukSayi[self.combo_Bas2.get()]))*int(10**sozlukSayi[self.combo_Carp.get()])
            elif self.bantSecim.get() == 5:
                self.netSayi=int(str(sozlukSayi[self.combo_Bas1.get()]) + str(sozlukSayi[self.combo_Bas2.get()])+str(sozlukSayi[self.combo_Bas3.get()]))*(10**sozlukSayi[self.combo_Carp.get()])
            self.maxSayi = (self.netSayi+(self.netSayi*sozlukTolerans[self.combo_Tol.get()])/100)
            self.minSayi = (self.netSayi-(self.netSayi*sozlukTolerans[self.combo_Tol.get()])/100)
            self.netDeger.set(str(self.netSayi) + " ohm")
            self.aralik.set(str(self.minSayi) + " - " + str(self.maxSayi) + " ohm")
            self.kanvasCiz()
        except:
            tkinter.messagebox.showerror("Hata","Lütfen gerekli bilgileri eksiksiz girin.")

    def kanvasCiz(self):
        self.kanvasTemizle()
        sozlukRenk = {"Siyah": "black", "Kahverengi": "saddle brown", "Kırmızı": "red", "Turuncu": "orange red", "Sarı": "yellow", "Yeşil": "green", "Mavi": "blue",
                      "Mor": "purple", "Gri": "gray", "Beyaz": "white", "Altın": "Darkgoldenrod1", "Gümüş": "light gray"}
        if self.bantSecim.get() == 4:
            self.bant1 = self.kanvas.create_rectangle(220, 20, 240, 80, tags="bant1",
                                                      outline=sozlukRenk[self.combo_Bas1.get()],
                                                      fill=sozlukRenk[self.combo_Bas1.get()])
            self.bant2 = self.kanvas.create_rectangle(260, 20, 280, 80, tags="bant2",
                                                      outline=sozlukRenk[self.combo_Bas2.get()],
                                                      fill=sozlukRenk[self.combo_Bas2.get()])
            self.bant3 = self.kanvas.create_rectangle(300, 20, 320, 80, tags="bant3",
                                                      outline=sozlukRenk[self.combo_Carp.get()],
                                                      fill=sozlukRenk[self.combo_Carp.get()])
            self.bant4 = self.kanvas.create_rectangle(360, 10, 380, 90, tags="bant4",
                                                      outline=sozlukRenk[self.combo_Tol.get()],
                                                      fill=sozlukRenk[self.combo_Tol.get()])
        elif self.bantSecim.get() == 5:
            self.bant1 = self.kanvas.create_rectangle(165, 10, 185, 90, tags="bant1",
                                                      outline=sozlukRenk[self.combo_Bas1.get()],
                                                      fill=sozlukRenk[self.combo_Bas1.get()])
            self.bant2 = self.kanvas.create_rectangle(220, 20, 240, 80, tags="bant2",
                                                      outline=sozlukRenk[self.combo_Bas2.get()],
                                                      fill=sozlukRenk[self.combo_Bas2.get()])
            self.bant3 = self.kanvas.create_rectangle(260, 20, 280, 80, tags="bant3",
                                                      outline=sozlukRenk[self.combo_Bas3.get()],
                                                      fill=sozlukRenk[self.combo_Bas3.get()])
            self.bant4 = self.kanvas.create_rectangle(300, 20, 320, 80, tags="bant4",
                                                      outline=sozlukRenk[self.combo_Carp.get()],
                                                      fill=sozlukRenk[self.combo_Carp.get()])
            self.bant5 = self.kanvas.create_rectangle(360, 10, 380, 90, tags="bant5",
                                                      outline=sozlukRenk[self.combo_Tol.get()],
                                                      fill=sozlukRenk[self.combo_Tol.get()])
    def kanvasTemizle(self):
        try:
            self.kanvas.delete(self.bant1)
            self.kanvas.delete(self.bant2)
            self.kanvas.delete(self.bant3)
            self.kanvas.delete(self.bant4)
            self.kanvas.delete(self.bant5)
        except:
            pass

basla=DirencHesaplayici()