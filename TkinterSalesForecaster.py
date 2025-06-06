import tkinter as tk
from tkinter import ttk, messagebox

def ortalama_hesapla(veriler, hafta_sayisi):
    if len(veriler) < hafta_sayisi:
        raise ValueError(f"Yeterli veri yok. Ortalama için en az {hafta_sayisi} haftalık veri gerekli.")
    
    ortalama = sum(veriler) / hafta_sayisi
    return ortalama

def tahmin_yap(hafta_sayisi_ortalama):
    try:
        tahmin_haftasi_str = hafta_secim.get()
        tahmin_haftasi_num = int(tahmin_haftasi_str.split('.')[0])
        
        start_index = tahmin_haftasi_num - hafta_sayisi_ortalama - 1
        end_index = tahmin_haftasi_num - 1

        if tahmin_haftasi_num <= hafta_sayisi_ortalama:
            messagebox.showerror("Hata", 
                                 f"Tahmin edilecek hafta ({tahmin_haftasi_num}) için yeterli geçmiş veri yok.\n"
                                 f"'{hafta_sayisi_ortalama} Haftalık' ortalama için en az {hafta_sayisi_ortalama + 1}. haftayı tahmin etmelisiniz.")
            return

        if start_index < 0 or end_index > len(veri_entryleri):
            messagebox.showerror("Hata", f"Tahmin edilecek hafta ({tahmin_haftasi_num}) için yeterli geçmiş veri mevcut değil. "
                                 f"Lütfen 'Tahmin Edilen Hafta' seçiminizi veya geçmiş veri girişlerini kontrol edin. "
                                 f"Giriş yapılmış veri sayısı: {len(veri_entryleri)}")
            return

        gecmis_veriler = []
        for i in range(start_index, end_index):
            try:
                gecmis_veriler.append(float(veri_entryleri[i].get()))
            except ValueError:
                messagebox.showerror("Hata", "Lütfen tahmin için gerekli tüm geçmiş satış verilerini (sayısal) doldurun.")
                return

        ortalama = ortalama_hesapla(gecmis_veriler, hafta_sayisi_ortalama)

        gercek_deger = float(gercek_entry.get())

        tahmin_sonuc_label.config(text=f"{tahmin_haftasi_str} tahmini : {ortalama:.2f}")
        gercek_label.config(text=f"{tahmin_haftasi_str} gerçekleşen : {gercek_deger}")
        hata_payi = abs((gercek_deger - ortalama) / gercek_deger) * 100
        hata_label.config(text=f"HATA PAYI : %{hata_payi:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen tüm girişleri sayısal girin.")
    except ZeroDivisionError:
        messagebox.showerror("Hata", "Gerçekleşen değer sıfır olamaz.")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen bir hata oluştu: {e}")

pencere = tk.Tk()
pencere.title("Haftalık Talep Tahmin Uygulaması")

veri_entryleri = []
for i in range(12):
    tk.Label(pencere, text=f"{i+1}. HAFTA VERİ:").grid(row=i, column=0, padx=5, pady=2, sticky='e')
    entry = tk.Entry(pencere, width=10)
    entry.grid(row=i, column=1, padx=5, pady=2)
    veri_entryleri.append(entry)

for i, val in enumerate([0, 594, 217, 339, 0, 360, 19, 349, 160, 13, 10, 0]):
    if i < len(veri_entryleri):
        veri_entryleri[i].insert(0, str(val))

aciklama = tk.Label(pencere, text="SEÇİM YAPMIŞ OLDUĞUNUZ HAFTADAN ÖNCEKİ 3 VE 6 HAFTA VERİLERİNİ GİRİP HESAPLAMA YAPABİLİRSİNİZ")
aciklama.grid(row=0, column=3, rowspan=3, padx=20, sticky='w')

tk.Label(pencere, text="Talep Tahmin Haftasını Seçiniz:").grid(row=12, column=0, pady=10)
haftalar = [f"{i+1}. Hafta" for i in range(12)]
hafta_secim = ttk.Combobox(pencere, values=haftalar, width=15)
hafta_secim.set("10. Hafta")
hafta_secim.grid(row=12, column=1)

tk.Label(pencere, text="Gerçekleşen Değer:").grid(row=13, column=0, pady=2)
gercek_entry = tk.Entry(pencere, width=10)
gercek_entry.grid(row=13, column=1)
gercek_entry.insert(0, "135")

tk.Button(pencere, text="3 HAFTALIK TALEP TAHMİNİ YAP", command=lambda: tahmin_yap(3)).grid(row=14, column=0, columnspan=2, pady=5)
tk.Button(pencere, text="6 HAFTALIK TALEP TAHMİNİ YAP", command=lambda: tahmin_yap(6)).grid(row=15, column=0, columnspan=2, pady=5)



tahmin_sonuc_label = tk.Label(pencere, text="Tahmin :")
tahmin_sonuc_label.grid(row=12, column=3, sticky='w', padx=10)
gercek_label = tk.Label(pencere, text="Gerçekleşen :")
gercek_label.grid(row=13, column=3, sticky='w', padx=10)
hata_label = tk.Label(pencere, text="HATA PAYI :")
hata_label.grid(row=14, column=3, sticky='w', padx=10)

pencere.mainloop()
