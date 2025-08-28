# Meyve Mağazası Satış Sistemi

# 1. Ürün Bilgisi Girişi
meyve_sayisi = int(input("Kaç çeşit meyve alacaksınız? "))

meyveler = []

for i in range(meyve_sayisi):
    ad = input(f"{i+1}. Meyve adı: ")
    fiyat = float(input(f"{i+1}. Birim fiyat (TL/kg): "))
    miktar = float(input(f"{i+1}. Alınacak miktar (kg): "))
    meyveler.append({'ad': ad, 'fiyat': fiyat, 'miktar': miktar})

# 2. KDV Hesaplaması
kdv_orani = 0.20
toplam_tutar_kdvsiz = 0
toplam_tutar_kdvli = 0
tutarlar = []  # KDV'siz tutarlar için

print("\nGirilen Bilgiler ve KDV Dahil Fiyatlar:")
for meyve in meyveler:
    tutar = meyve['fiyat'] * meyve['miktar']
    kdv_dahil = tutar * (1 + kdv_orani)
    meyve['tutar'] = tutar
    meyve['kdv_dahil'] = kdv_dahil
    tutarlar.append(tutar)
    
    print(f"Meyve: {meyve['ad']}, Birim Fiyat: {meyve['fiyat']} TL/kg, Miktar: {meyve['miktar']} kg, KDV Dahil Tutar: {kdv_dahil:.2f} TL")
    
    toplam_tutar_kdvsiz += tutar
    toplam_tutar_kdvli += kdv_dahil

# 3. Çıktı Gösterimi
print(f"\nToplam Tutar (KDV'siz): {toplam_tutar_kdvsiz:.2f} TL")
print(f"Toplam Tutar (KDV Dahil): {toplam_tutar_kdvli:.2f} TL")

# 4. İstatistik Analizi
if meyve_sayisi > 0:
    en_pahali = max(meyveler, key=lambda x: x['fiyat'])
    en_ucuz = min(meyveler, key=lambda x: x['fiyat'])
    ortalama_tutar = sum(tutarlar) / meyve_sayisi
    toplam_miktar = sum(meyve['miktar'] for meyve in meyveler)
    
    print("\nİstatistik Analizi:")
    print(f"En Pahalı Ürün: {en_pahali['ad']} ({en_pahali['fiyat']} TL/kg)")
    print(f"En Ucuz Ürün: {en_ucuz['ad']} ({en_ucuz['fiyat']} TL/kg)")
    print(f"Ortalama Ürün Tutarı (KDV Hariç): {ortalama_tutar:.2f} TL")
    print(f"Toplam Alınacak Meyve Miktarı: {toplam_miktar:.2f} kg")

# 5. Sıralama Özellikleri
sirali_meyveler = sorted(meyveler, key=lambda x: x['fiyat'], reverse=True)

print("\nÜrünler Fiyata Göre Azalan Sırada (Birim Fiyat):")
for meyve in sirali_meyveler:
    print(f"{meyve['ad']}: {meyve['fiyat']} TL/kg")