import os

def read_existing_numbers(filename):
    """
    item_names.txt dosyasından VNUM değerlerini okur
    Dosya formatı: VNUM\tLOCALE_NAME (tab ile ayrılmış)
    """
    existing_numbers = set()
    
    # Farklı encoding'leri dene
    encodings = ['utf-8', 'cp1254', 'latin-1', 'iso-8859-9', 'windows-1254']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                print(f"✓ Dosya {encoding} kodlaması ile okunuyor...")
                
                line_count = 0
                for line in file:
                    line_count += 1
                    line = line.strip()
                    
                    # Boş satırları atla
                    if not line:
                        continue
                    
                    # Header satırını atla (VNUM	LOCALE_NAME)
                    if line_count == 1 and ('VNUM' in line and 'LOCALE' in line):
                        print("✓ Header satırı atlandı")
                        continue
                    
                    # Tab ile böl
                    parts = line.split('\t')
                    if len(parts) >= 1:
                        vnum = parts[0].strip()
                        if vnum.isdigit():  # VNUM sayı mı kontrol et
                            existing_numbers.add(int(vnum))
                
                print(f"✓ Toplam {len(existing_numbers)} VNUM okundu")
                return existing_numbers  # Başarılı okuma
                
        except UnicodeDecodeError:
            continue  # Bu encoding çalışmazsa bir sonrakini dene
        except FileNotFoundError:
            print(f"HATA: {filename} dosyası bulunamadı!")
            return None
        except Exception as e:
            print(f"HATA: Dosya okuma hatası ({encoding}) - {e}")
            continue
    
    # Hiçbir encoding çalışmazsa
    print("HATA: Dosya hiçbir karakter kodlaması ile okunamadı!")
    print("Desteklenen kodlamalar:", ", ".join(encodings))
    return None

def find_available_numbers(existing_numbers, count, start_range=1, end_range=10000, consecutive=False):
    """
    Belirtilen aralıkta boşta olan numaraları bulur
    consecutive=True ise ardışık numaralar döner
    """
    if not consecutive:
        # Normal mod - herhangi boş numaralar
        available_numbers = []
        for num in range(start_range, end_range + 1):
            if num not in existing_numbers:
                available_numbers.append(num)
                if len(available_numbers) >= count:
                    break
        return available_numbers
    
    else:
        # Ardışık mod - peş peşe boş numaralar
        available_numbers = []
        consecutive_count = 0
        start_consecutive = None
        
        for num in range(start_range, end_range + 1):
            if num not in existing_numbers:
                if consecutive_count == 0:
                    start_consecutive = num
                consecutive_count += 1
                
                if consecutive_count >= count:
                    # Yeterli ardışık numara bulundu
                    available_numbers = list(range(start_consecutive, start_consecutive + count))
                    break
            else:
                # Ardışık dizi kırıldı, sıfırla
                consecutive_count = 0
                start_consecutive = None
        
        return available_numbers

def main():
    filename = "item_names.txt"
    
    print("=== BOŞ ITEM NUMARASI BULUCU ===")
    print()
    
    # Dosya varlığını kontrol et
    if not os.path.exists(filename):
        print(f"HATA: {filename} dosyası mevcut dizinde bulunamadı!")
        print("Lütfen item_names.txt dosyasının bu Python dosyasıyla aynı klasörde olduğundan emin olun.")
        return
    
    # Mevcut numaraları oku
    existing_numbers = read_existing_numbers(filename)
    if existing_numbers is None:
        return
    
    print(f"✓ {filename} dosyası başarıyla okundu")
    print(f"✓ Toplam {len(existing_numbers)} adet item numarası bulundu")
    
    if existing_numbers:
        print(f"✓ En küçük numara: {min(existing_numbers)}")
        print(f"✓ En büyük numara: {max(existing_numbers)}")
    
    print()
    
    # Kullanıcıdan kaç tane boş numara istediğini sor
    while True:
        try:
            count = int(input("Kaç tane boş numara istersiniz? "))
            if count > 0:
                break
            else:
                print("Lütfen pozitif bir sayı girin!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    
    # Ardışık numara seçeneği
    print()
    consecutive_input = input("Numaraları ardışık mı istersiniz? (e/h, varsayılan: h): ").strip().lower()
    consecutive = consecutive_input in ['e', 'evet', 'yes', 'y']
    
    if consecutive:
        print(f"✓ {count} adet ardışık boş numara aranacak")
    else:
        print(f"✓ {count} adet herhangi boş numara aranacak")
    
    # Aralık seçimi (opsiyonel)
    print("\nAralık seçimi (Enter'a basarak varsayılan değerleri kullanabilirsiniz):")
    try:
        start_input = input("Başlangıç numarası (varsayılan: 1): ").strip()
        start_range = int(start_input) if start_input else 1
        
        end_input = input("Bitiş numarası (varsayılan: 10000): ").strip()
        end_range = int(end_input) if end_input else 10000
        
        if start_range >= end_range:
            print("Başlangıç numarası bitiş numarasından küçük olmalı! Varsayılan değerler kullanılıyor.")
            start_range, end_range = 1, 10000
            
    except ValueError:
        print("Geçersiz aralık girişi! Varsayılan değerler kullanılıyor.")
        start_range, end_range = 1, 10000
    
    # Boş numaraları bul
    available_numbers = find_available_numbers(existing_numbers, count, start_range, end_range, consecutive)
    
    print(f"\n=== SONUÇLAR ===")
    print(f"Aralık: {start_range} - {end_range}")
    print(f"Mod: {'Ardışık' if consecutive else 'Rastgele'}")
    
    if len(available_numbers) == count:
        print(f"✓ İstediğiniz {count} adet boş numara bulundu:")
        print()
        
        # Numaraları güzel bir formatta göster
        for i, num in enumerate(available_numbers, 1):
            print(f"{i:2d}. {num}")
            
        print(f"\nBoş numaralar (kopyalamak için): {', '.join(map(str, available_numbers))}")
        
        # Ardışık modda aralık göster
        if consecutive and available_numbers:
            print(f"Ardışık aralık: {available_numbers[0]} - {available_numbers[-1]}")
        
    elif len(available_numbers) > 0:
        print(f"⚠ Sadece {len(available_numbers)} adet boş numara bulunabildi:")
        print()
        
        for i, num in enumerate(available_numbers, 1):
            print(f"{i:2d}. {num}")
            
        print(f"\nBoş numaralar: {', '.join(map(str, available_numbers))}")
        
        if consecutive:
            print("Not: Yeterli ardışık boş numara bulunamadı!")
        
    else:
        print("❌ Belirtilen aralıkta boş numara bulunamadı!")
        if consecutive:
            print(f"Not: {count} adet ardışık boş numara bulunamadı. Daha geniş aralık deneyin veya ardışık seçeneğini kapatın.")
        else:
            print("Daha geniş bir aralık deneyebilirsiniz.")

if __name__ == "__main__":
    main()