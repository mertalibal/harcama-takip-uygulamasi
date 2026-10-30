import re

def kullanicilar():
    kullanici_sifreleri = []
    kullanici_adlari = []
    with open("kullanicilar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            kullanici_sifresi_ = satir.split(":")[1].split(",")[1].strip()
            kullanici_sifreleri.append(kullanici_sifresi_)
            kullanici_adi_ = satir.split(":")[1].split(",")[0].strip().lower()
            kullanici_adlari.append(kullanici_adi_)
    return kullanici_sifreleri, kullanici_adlari

def kayit_ol():
    _, kullanici_adlari = kullanicilar()
    while True:
        kullanici_adi = input("\nKullanici adinizi giriniz: ")
        if not re.fullmatch(r"[a-zA-Z0-9._]+", kullanici_adi):
            print("Kullanici adi sadece Ingilizce harf, rakam, alt cizgi ve nokta icerebilir!")
            continue
        elif kullanici_adi.startswith(".") or kullanici_adi.endswith(".") or ".." in kullanici_adi:
            print("Nokta kullanimi hatali!")
        elif len(kullanici_adi) > 30:
            print("Kullanici adi en fazla 30 karakter olabilir!")
        elif re.search(r"\s", kullanici_adi):
            print("Kullanici adiniz bosluk iceremez!")
        else:
            kullanici_adi = kullanici_adi.lower().strip()
            if kullanici_adi in kullanici_adlari:
                print("Bu kullanici adi zaten alinmis!")
                continue
            break
    while True:
        kullanici_sifre = input("Sifrenizi giriniz: ")
        if len(kullanici_sifre) < 8:
            print("Parola en az 8 karakter olmalidir!")
        elif not re.search("[a-z]", kullanici_sifre):
            print("Parola kucuk harf icermelidir!")
        elif not re.search("[A-Z]", kullanici_sifre):
            print("Parola buyuk harf icermelidir!")
        elif not re.search("[0-9]", kullanici_sifre):
            print("Parola rakam icermelidir!")
        elif not re.search(r"""[!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~£½₺¨´^°˘¯¸]""", kullanici_sifre):
            print("Parola ozel karakter icermelidir!")
        elif re.search(r"\s", kullanici_sifre):
            print("Parola bosluk icermemelidir!")
        else:
            break
    while True:
        print("\nCikmak icin 5 yaziniz")
        sifre_kontrol = input("Sifrenizi tekrardan giriniz: ")
        if sifre_kontrol == "5":
            break
        elif sifre_kontrol == kullanici_sifre:
            with open("kullanicilar.txt", "a", encoding="utf-8") as file:
                file.write(f"Kullanici: {kullanici_adi}, {kullanici_sifre}\n")
                print("Basariyla kayit oldunuz!")
            break
        else:
            print("\nSifreler uyusmuyor.")

def giris_yap():
    kullanici_sifreleri, kullanici_adlari = kullanicilar()
    while True:
        print("\nCikis yapmak icin 5'i tuslayiniz.")
        kullanici_adi = input("Kullanici adinizi giriniz: ")
        kullanici_adi = kullanici_adi.lower().strip()
        if kullanici_adi == "5":
            break
        elif kullanici_adi not in kullanici_adlari:
            print("Kullanici adi bulunamadi!")
            continue
        kullanici_indexi = kullanici_adlari.index(kullanici_adi)
        kullanici_sifresi = input("Sifrenizi giriniz: ")
        if kullanici_sifresi == kullanici_sifreleri[kullanici_indexi]:
            print("Basarili bir sekilde giris yaptiniz!\n")
            return kullanici_adi
        else:
            print("Parolanizi hatali girdiniz!")
            continue
    
