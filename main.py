import tkinter as tk

def gorev_ekle():
 yeni_gorev=gorev_giris.get()
 if yeni_gorev:
   gorevler.append({"gorev":yeni_gorev,"yapıldı":False})
   gorev_listesi.insert(tk.END,yeni_gorev)
   gorev_giris.delete(0,tk.END)



def gorev_sil():
 secili_index=gorev_listesi.curselection()
 if secili_index:
  gorevler.pop(secili_index[0])
  gorev_listesi.delete(secili_index)



def gorev_yapildi():
 secili_index=gorev_listesi.curselection()
 if secili_index:
   gorevler[secili_index[0]]["yapıldı"]=True
   yeni_metin=gorevler[secili_index[0]]["gorev"]+("yapıldı")
   gorev_listesi.delete(secili_index[0])
   gorev_listesi.insert(secili_index[0],yeni_metin)
   gorev_listesi.itemconfig(secili_index[0],fg="green")


gorevler=[]

ana_pencere=tk.Tk()
ana_pencere.title("Gorev_Listesi")

gorev_giris=tk.Entry(ana_pencere,width=40)
gorev_giris.pack(pady=5)

ekle_buton=tk.Button(ana_pencere,text="Görev Ekle",command=gorev_ekle)
ekle_buton.pack(pady=5)


gorev_listesi=tk.Listbox(ana_pencere,width=50,height=15)
gorev_listesi.pack(pady=10)


sil_buton=tk.Button(ana_pencere,text="Seçilen Görevi Sil",command=gorev_sil)
sil_buton.pack(pady=5)

yapildi_buton=tk.Button(ana_pencere,text="Yapıldı Olarak İşaretle",command=gorev_yapildi)
yapildi_buton.pack(pady=5)



ana_pencere.mainloop()


