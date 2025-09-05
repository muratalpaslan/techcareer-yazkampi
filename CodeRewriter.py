def urun_bilgisi_girisi():
    """Kullanıcıdan meyve bilgilerini alır ve bir liste olarak döndürür."""
    meyve_sayisi = int(input("Kaç çeşit meyve alacaksınız? "))
    meyveler = []
    
    for i in range(meyve_sayisi):
        ad = input(f"{i+1}. Meyve adı: ")
        fiyat = float(input(f"{i+1}. Birim fiyat (TL/kg): "))
        miktar = float(input(f"{i+1}. Alınacak miktar (kg): "))
        meyveler.append({'ad': ad, 'fiyat': fiyat, 'miktar': miktar})
    
    return meyveler

def kdv_hesapla(meyveler, kdv_orani=0.20):
    """Meyveler için KDV dahil tutarları hesaplar ve toplamları döndürür."""
    toplam_tutar_kdvsiz = 0
    toplam_tutar_kdvli = 0
    tutarlar = []
    
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
    
    return toplam_tutar_kdvsiz, toplam_tutar_kdvli, tutarlar

def cikti_goster(toplam_tutar_kdvsiz, toplam_tutar_kdvli):
    """Toplam tutarları ekrana yazdırır."""
    print(f"\nToplam Tutar (KDV'siz): {toplam_tutar_kdvsiz:.2f} TL")
    print(f"Toplam Tutar (KDV Dahil): {toplam_tutar_kdvli:.2f} TL")

def istatistik_analizi(meyveler, tutarlar):
    """Meyveler için istatistiksel analiz yapar ve sonuçları ekrana yazdırır."""
    if meyveler:
        en_pahali = max(meyveler, key=lambda x: x['fiyat'])
        en_ucuz = min(meyveler, key=lambda x: x['fiyat'])
        ortalama_tutar = sum(tutarlar) / len(meyveler)
        toplam_miktar = sum(meyve['miktar'] for meyve in meyveler)
        
        print("\nİstatistik Analizi:")
        print(f"En Pahalı Ürün: {en_pahali['ad']} ({en_pahali['fiyat']} TL/kg)")
        print(f"En Ucuz Ürün: {en_ucuz['ad']} ({en_ucuz['fiyat']} TL/kg)")
        print(f"Ortalama Ürün Tutarı (KDV Hariç): {ortalama_tutar:.2f} TL")
        print(f"Toplam Alınacak Meyve Miktarı: {toplam_miktar:.2f} kg")

def fiyata_gore_sirala(meyveler):
    """Meyveleri birim fiyata göre azalan sırada sıralar ve ekrana yazdırır."""
    sirali_meyveler = sorted(meyveler, key=lambda x: x['fiyat'], reverse=True)
    
    print("\nÜrünler Fiyata Göre Azalan Sırada (Birim Fiyat):")
    for meyve in sirali_meyveler:
        print(f"{meyve['ad']}: {meyve['fiyat']} TL/kg")

def main():
    """Ana fonksiyon: Programın akışını yönetir."""
    meyveler = urun_bilgisi_girisi()
    toplam_tutar_kdvsiz, toplam_tutar_kdvli, tutarlar = kdv_hesapla(meyveler)
    cikti_goster(toplam_tutar_kdvsiz, toplam_tutar_kdvli)
    istatistik_analizi(meyveler, tutarlar)
    fiyata_gore_sirala(meyveler)

if __name__ == "__main__":
    main()