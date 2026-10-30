from yonetici import harcama_ekle, harcama_listele, harcama_topla, kategori_filtreleme, dosyadan_harcama_cekme, harcamayi_dosyaya_kaydet, harcama_sil  
from kullanici import kayit_ol, giris_yap

while True:
    islem = input("1- Kayit Ol\n2- Giris Yap\n3- Cikis\nYapmak Istediginiz Islemi Seciniz: ")
    if islem == "1":
        kayit_ol()
    elif islem == "2":
        a = giris_yap()
        if a is None:
            continue
        else:
            dosya_adi = a + "_harcamalar.txt"
            harcamalar = []
            dosyadan_harcama_cekme(dosya_adi, harcamalar)
            while True:
                islem = input("1- Harcama Ekle\n2- Harcama Listesini Goster\n" \
                "3- Toplam Harcamayi Goster\n4- Kategoriye Gore Filtrele\n5- Harcama Sil\n" \
                "6- Cikis\nYapmak Istediginiz Islemi Seciniz: ")
                if islem == "1":
                    harcama = harcama_ekle()
                    harcamalar.append(harcama)
                    harcamayi_dosyaya_kaydet(dosya_adi, harcama)
                elif islem == "2":
                    harcama_listele(harcamalar)
                elif islem == "3":
                    harcama_topla(harcamalar)
                elif islem == "4":
                    kategori_filtreleme(harcamalar)
                elif islem == "5":
                    harcama_sil(dosya_adi, harcamalar)
                elif islem == "6":
                    print("Ana menuye donuluyor...\n")
                    break
                else:
                    print("\nLutfen gecerli islem giriniz!\n")
    elif islem == "3":
        print("\nBizi tercih ettiginiz icin tesekkurler!")
        break
    else:
        print("\nLutfen gecerli islem giriniz!\n")
