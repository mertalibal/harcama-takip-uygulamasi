# 💰 Harcama Takip Uygulaması

Python kullanılarak geliştirilen, kullanıcı kayıt ve giriş sistemi bulunan kişisel harcama takip uygulaması.

Uygulama sayesinde kullanıcılar kendi hesapları üzerinden harcamalarını ekleyebilir, listeleyebilir, toplam harcamalarını görüntüleyebilir, kategorilere göre filtreleyebilir ve istedikleri harcamaları silebilir.

## ✨ Özellikler

- **Kullanıcı Kaydı:** Yeni kullanıcı hesabı oluşturma.
- **Kullanıcı Girişi:** Kullanıcı adı ve şifre ile giriş yapma.
- **Şifre Kontrolü:** Kayıt sırasında belirli şifre kurallarını doğrulama.
- **Harcama Ekleme:** Harcama adı, tutarı ve kategorisi girerek kayıt oluşturma.
- **Harcama Listeleme:** Kayıtlı harcamaları görüntüleme.
- **Toplam Harcama:** Tüm harcamaların toplam tutarını hesaplama.
- **Kategoriye Göre Filtreleme:** Harcamaları kategorilerine göre görüntüleme.
- **Harcama Silme:** İstenilen harcamayı onay ile silme.
- **Veri Saklama:** Harcamaları metin dosyalarında saklayarak uygulama kapatıldığında verilerin korunmasını sağlama.
- **Kullanıcıya Özel Veriler:** Her kullanıcının harcamalarını ayrı dosyalarda tutma.

## 🛠️ Kullanılan Teknolojiler

- Python
- Nesne Yönelimli Programlama (OOP)
- Fonksiyonlar ve Modüler Programlama
- Dosya İşlemleri
- Liste ve Sınıflar
- Hata Yönetimi
- Regular Expressions (Regex)

## 📁 Proje Dosya Yapısı

```text
harcama-takip-uygulamasi/
│
├── main.py
├── harcama.py
├── yonetici.py
├── kullanici.py
├── README.md
└── .gitignore
```

## 🚀 Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza indirin veya klonlayın.

```bash
git clone https://github.com/mertalibal/harcama-takip-uygulamasi.git
```

2. Proje klasörüne girin.

```bash
cd harcama-takip-uygulamasi
```

3. Uygulamayı çalıştırın.

```bash
python main.py
```

## 📌 Geliştirme Hakkında

Bu proje Python öğrenme sürecinde geliştirilen bir uygulamadır. Nesne yönelimli programlama, modüler yapı, dosya yönetimi ve kullanıcı işlemleri gibi konularda pratik yapmak amacıyla oluşturulmuştur.

## ⚠️ Güvenlik Notu

Bu proje eğitim amaçlıdır. Mevcut sürümde kullanıcı şifreleri metin dosyasında düz metin olarak saklanmaktadır. Gerçek kullanıcı hesapları için güvenli parola hashleme yöntemleri kullanılmalıdır.

## 👨‍💻 Geliştirici

**Mert Ali Bal**

GitHub: [@mertalibal](https://github.com/mertalibal)
