# LISTE METOTLARI
notlar = [85, 92, 76, 92, 100, 76, 85, 92]

# 1) Tekrarları silip, ilk görülen sıralamayı koruyarak benzersiz liste
benzersiz = []
for n in notlar:
    if n not in benzersiz:
        benzersiz.append(n)

# 2) En yüksek ve en düşük
en_yuksek = max(notlar)
en_dusuk  = min(notlar)

# 3) Küçükten büyüğe sıralama
sirali = sorted(notlar)

print("Benzersiz (orijinal sırayla):", benzersiz)
print("En yüksek:", en_yuksek, " | En düşük:", en_dusuk)
print("Sıralı:", sirali)


#SAYILAR
def armstrong_mu(sayi):
    toplam = 0
    for basamak in str(sayi):  # sayıyı stringe çevirip her basamağı alıyoruz
        toplam += int(basamak) ** 3  # her basamağın küpünü toplama ekliyoruz
    
    if toplam == sayi:
        return True
    else:
        return False


# Örnek testler
testler = [0, 1, 153, 370, 371, 407, 123]
for t in testler:
    print(t, "→", armstrong_mu(t))


# KÜMELER
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

ortak = A & B
sadece_A = A - B
birlesim_alfabetik = sorted(A | B)

print("Ortak:", ortak)
print("Sadece A:", sadece_A)
print("Birleşim (A→Z):", birlesim_alfabetik)


# MODÜLLER
import random
import statistics

# 1–100 arasında 10 rastgele sayı
sayilar = [random.randint(1, 100) for _ in range(10)]

ortalama = statistics.mean(sayilar)
# örneklem std sapma (n-1): stdev — çoğu pratikte bu kullanılır
std_sapma = statistics.stdev(sayilar)

print("Sayılar:", sayilar)
print("Ortalama:", ortalama)
print("Standart Sapma (örneklem):", std_sapma)


# FONKSIYONLAR
def kelime_sayaci(metin: str):
    # basit noktalama temizliği
    temiz = []
    for parca in metin.lower().split():
        kelime = parca.strip(".,;:!?()[]{}\"'")  # temel temizlik
        if kelime:
            temiz.append(kelime)

    if not temiz:
        return {"toplam_kelime": 0, "en_uzun": "", "en_sik": ""}

    # toplam kelime sayısı
    toplam = len(temiz)

    # en uzun kelime
    en_uzun = max(temiz, key=len)

    # frekans sayımı (Counter kullanmadan)
    sayim = {}
    for k in temiz:
        sayim[k] = sayim.get(k, 0) + 1

    # en sık kelime (eşitlikte alfabetik küçük olan)
    en_sik = ""
    en_cok = -1
    for k, adet in sayim.items():
        if adet > en_cok or (adet == en_cok and k < en_sik):
            en_sik = k
            en_cok = adet

    return {"toplam_kelime": toplam, "en_uzun": en_uzun, "en_sik": en_sik}


# küçük test
# print(kelime_sayaci("Veri bilim veri ANALİZ bilim Python python python!"))


# GÖMÜLÜ FONKSİYONLAR
sayilar = [5, 12, 7, 18, 24, 3, 16]

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
kareler = list(map(lambda x: x**2, ciftler))
azalan = sorted(kareler, reverse=True)

print("Çiftler:", ciftler)
print("Kareler:", kareler)
print("Kareler (azalan):", azalan)


# LAMBDA İFADELER
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
sonuc = sorted(kelimeler, key=lambda k: len(k))
print(sonuc)
# ['veri', 'bilim', 'analiz', 'python', 'yapayzeka']


# METODLAR 
def sayi_blok_toplami(s: str) -> int:
    toplam = 0
    biriken = ""  # ardışık rakamları burada biriktir

    for ch in s:
        if ch.isdigit():
            biriken += ch
        else:
            if biriken != "":
                toplam += int(biriken)
                biriken = ""
    # string rakamla bittiyse son bloğu ekle
    if biriken != "":
        toplam += int(biriken)

    return toplam

# örnekler
# print(sayi_blok_toplami("abc12def3"))   # 15
# print(sayi_blok_toplami("a0b007x5y"))   # 12 (0 + 7 + 5)
# print(sayi_blok_toplami("sayı yok!"))   # 0