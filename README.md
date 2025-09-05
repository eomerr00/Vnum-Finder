# Vnum-Finder
Created with AI
📦 Boş Item Numarası Bulucu

Python ile yazılmış bu araç, item_names.txt dosyasındaki mevcut VNUM (item numarası) verilerini analiz eder ve belirtilen aralıkta boşta olan numaraları bulur.

Hem rastgele boş numaraları hem de ardışık boş numara gruplarını destekler.

🧰 Özellikler

item_names.txt dosyasındaki VNUM verilerini otomatik olarak okur.

Farklı karakter kodlamalarını (UTF-8, CP1254, Latin-1 vs.) destekler.

Belirli bir aralıkta boş numaraları arar.

Ardışık ya da rastgele boş numaralar listelenebilir.

Uygun formatta çıktı sağlar.

Türkçe kullanıcı arayüzü ile kolay kullanım.

📂 Dosya Formatı

Script, aşağıdaki gibi bir item_names.txt dosyası bekler:

VNUM	LOCALE_NAME
1001	Kılıç
1002	Kalkan
...


VNUM: Item numarası (sayı)

LOCALE_NAME: İsim (önemsiz, sadece VNUM kullanılır)

🚀 Nasıl Kullanılır?
1. Gereksinimler

Python 3.x yüklü olmalıdır. Harici bir kütüphane gerekmez.

2. Kurulum
git clone <repo-url>
cd <repo-dizini>

3. item_names.txt dosyasını aynı klasöre yerleştirin.
4. Script'i çalıştırın
python script_adi.py

👇 Kullanım Adımları

Kaç adet boş numara istediğinizi girin.

Numaraların ardışık olup olmayacağını belirtin.

(İsteğe bağlı) Aralık girin (Başlangıç, Bitiş). Enter ile varsayılan değerler (1-10000) kullanılır.

Script, sonucu ekrana yazdırır ve kopyalanabilir formatta gösterir.

🧪 Örnek Çıktı
Kaç tane boş numara istersiniz? 5
Numaraları ardışık mı istersiniz? (e/h): e
Başlangıç numarası: 1000
Bitiş numarası: 2000

=== SONUÇLAR ===
Aralık: 1000 - 2000
Mod: Ardışık
✓ İstediğiniz 5 adet boş numara bulundu:

 1. 1035
 2. 1036
 3. 1037
 4. 1038
 5. 1039

Boş numaralar (kopyalamak için): 1035, 1036, 1037, 1038, 1039
Ardışık aralık: 1035 - 1039

⚠️ Hatalar ve Uyarılar

Dosya bulunamazsa:
HATA: item_names.txt dosyası mevcut dizinde bulunamadı!

Dosya okunamazsa:
HATA: Dosya hiçbir karakter kodlaması ile okunamadı!

Ardışık boş numara bulunamazsa:
Yeterli ardışık boş numara bulunamadı.

📄 Lisans

Bu proje herhangi bir lisans altında değildir. Dilerseniz kendi projelerinizde serbestçe kullanabilirsiniz.

✍️ Yazılım Geliştirici Notları

Kod okunabilirliği için yorumlar ve uyarılar eklenmiştir.

Türkçe kullanıcı arayüzü ile, teknik bilgisi az olan kişiler de kullanabilir.

Daha sonra GUI (arayüz) ile geliştirilebilir.
