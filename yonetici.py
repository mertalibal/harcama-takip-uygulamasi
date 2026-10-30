from harcama import Harcama
def kategori_sec():
    kategoriler = {
    "1": "Yemek",
    "2": "Market",
    "3": "Ulasim",
    "4": "Giyim",
    "5": "Temizlik",
    "6": "Kisisel Bakim",
    "7": "Eglence",
    "8": "Egitim",
    "9": "Faturalar",
    "10": "Kira",
    "11": "Saglik",
    "12": "Spor",
    "13": "Teknoloji",
    "14": "Abonelikler",
    "15": "Diger"
    }
    for key, value in kategoriler.items():
        print(key, value)
    while True:
        kategori_turu = input("Kategori seciniz: ")
        if kategori_turu in kategoriler:
            harcama_kategorisi = kategoriler[kategori_turu]
            break
        else:
            print("\nHata kategori bulunamadi!\n")
    return harcama_kategorisi

def harcama_ekle():
    harcama_adi =input("Harcama adini giriniz: ")
    while True:
        try:
            harcama_tutari = input("Harcama tutarini giriniz: ")
            harcama_tutari = float(harcama_tutari.replace(",","."))
            if harcama_tutari > 0:
                break
            elif harcama_tutari <= 0:
                print("\nHarcama tutari pozitif girilmelidir!\n")
        except ValueError:
            print("\nHarcama tutari sayi seklinde girilmelidir!\n")
    harcama_kategorisi = kategori_sec()
    harcama_bilgisi = Harcama(harcama_adi, harcama_tutari, harcama_kategorisi)
    print("\nHarcama basariyla eklendi!\n")
    return harcama_bilgisi

def harcama_listele(harcamalar):
    if not harcamalar:
        print("\nListeye ekleme yapmadiniz!\n")
    else:
        for i in range(len(harcamalar)):
            print(f"\n---Harcama {i+1}---")
            print(harcamalar[i].harcama_adi)
            print(harcamalar[i].harcama_tutari)
            print(f"{harcamalar[i].harcama_kategorisi}\n")

def harcama_topla(harcamalar):
    toplam = 0
    for i in range(len(harcamalar)):
        toplam += float(harcamalar[i].harcama_tutari)
    print(f"\nToplam = {toplam}\n")

def kategori_filtreleme(harcamalar):
    harcama_kategorisi = kategori_sec()
    degisken = True
    for i in range(len(harcamalar)):
        if harcama_kategorisi == harcamalar[i].harcama_kategorisi:
            print(f"\n{harcamalar[i].harcama_adi}")
            print(harcamalar[i].harcama_tutari)
            print(f"{harcamalar[i].harcama_kategorisi}\n")
            degisken = False
    if degisken:
        print("\nListelenecek harcama bulunamadi.\n")

def dosyadan_harcama_cekme(dosya_adi, harcamalar):
    with open(dosya_adi, "a+", encoding="utf-8") as file:
        file.seek(0)
        for satir in file:
            harcama = satir.strip().split(",")
            harcama = Harcama(harcama[0].strip(),float(harcama[1].strip()),harcama[2].strip())
            harcamalar.append(harcama)

def harcamayi_dosyaya_kaydet(dosya_adi, harcama):
    with open(dosya_adi, "a", encoding="utf-8") as file:
        file.write(f"{harcama.harcama_adi}, {harcama.harcama_tutari}, {harcama.harcama_kategorisi}\n")

def harcama_sil(dosya_adi, harcamalar):
    if len(harcamalar) == 0:
        print("Liste bos simdilik burada isin yok!")
    else:
        harcama_listele(harcamalar)
        while True:
            try:
                numara = int(input("Silmek istediginiz harcamanin numarasini giriniz: "))     
                if numara < 1 or numara > len(harcamalar):
                    print("Harcama bulunamadi!\n")
                else:
                    break
            except ValueError:
                print("Lutfen sayi giriniz: ")
        while True:
            onay = input("Bu harcamayi silmek istediginize emin misiniz(E/H)? :")
            onay = onay.lower().strip()
            if onay == "e":
                harcamalar.pop(numara - 1)
                with open(dosya_adi, "w", encoding="utf-8") as file:
                    for i in harcamalar:
                        file.write(f"{i.harcama_adi}, {i.harcama_tutari}, {i.harcama_kategorisi}\n")
                print("Basariyla silindi!\n")
                break
            elif onay == "h":
                print("Silme islemi iptal edildi!\n")    
                break
            else:
                print("Hatali tuslama!\n")

            
    
