#Bu ödevler koşullu ifadeler,döngüler ve temel veri işleme becerilerini geliştirmek için yapılmıştır.
#try - catch ya da diğer kontrol metotları göz ardı edilmiştir.

# 1- Sayı analizi

sayi = int(input('Sayı giriniz\n:'))

# Negatif - Pozitif - Sıfır
if sayi > 0:
    print(f"{sayi} pozitif sayıdır")
elif sayi < 0:
    print(f"{sayi} sayısı negatif sayıdır")
else:
    print(f"{sayi} sayısı sıfırdır.")

# Tek - Çift
if sayi % 2 == 0:
    print(f"{sayi} çift sayıdır")
elif sayi % 2 == 1: 
    print(f"{sayi} tek sayıdır")

# Pozitif/Negatif - Tek/Çift
if sayi > 0:
    if sayi % 2 == 0:
        print(f"{sayi} sayısı pozitif çift sayıdır")
    else:
        print(f"{sayi} sayısı pozitift tek sayıdır")
elif sayi < 0:
    if sayi % 2 == 0:
        print(f"{sayi} sayısı negatif çift sayıdır")
    else:
        print(f"{sayi} sayısı negatif tek sayıdır")
else:
    print('Sayı sıfırdır')

# 2- Harf Sayaç
kelime = input('Kelimeyi girin:\n')

sonuc = {}
for harf in kelime:
    if harf in sonuc:
        sonuc[harf] += 1
    else:
        sonuc[harf] = 1


print(sonuc)

# 3- Şifre Kontrolü

while True:
    buyukHarf = False
    isDigit = False

    sifre = input('Şifrenizi Giriniz: ')
    
    for karakter in sifre:
        if karakter.isupper():
            buyukHarf = True
        if karakter.isdigit():
            isDigit = True
        if buyukHarf and isDigit:
            break
    
    if ((len(sifre) < 8) or (buyukHarf is False) or (isDigit is False)):
        print('şifreniz en az 8 karakterten oluşup, büyük harf ve rakam içermelidir. ')
    else:
        print('Şifre başarıyla oluşturuldu.')
        break

# 4- Liste İşlemleri

liste = [12, 4, 9, 25, 30, 7, 18]

# Ortalamayı bulma
toplam = 0
for say in liste:
    toplam += say

ortalama = toplam/ len(liste)

# Büyükleri bulma
bigger = []
for say in liste:
    if say > ortalama:
        bigger.append(say)

print(f"Listenin ortalaması {ortalama} ve ortalamanın üzerindeki sayıların listesi\n:{bigger}")


# 5- Yıldız
for sayi in range(6):
    print(sayi*'*')

# 6- While Döngüsü
toplam = 0

while True:
    sayi = int(input('Sayi girin (Çıkmak için 0 tuşuna basın): '))
    if sayi == 0:
        print('Çıkış yapılıyor...')
        break
    else:
        toplam += sayi
    
    print(f"Sayıların toplamı {toplam}\n")

# 7- Palindrom
kelime = input("Kelimeyi girin: ").lower()

if kelime == kelime[::-1]:
    print("Palindrom")
else:
    print("Palindrom değil")

# 8- List Comprehesion 
karesi = [sayi**2 for sayi in range(1, 101) if sayi % 3 == 0 and sayi % 5 == 0]
print(karesi)

# 9- String İşlemleri
cumle = input('Bana bir cümle ver: ')

splinterUsta = cumle.split()

print(splinterUsta)
print(cumle.title())

# 10- Mini Proje

yorumlar = []

for izleyici in range(7):
    yorum = input(f"film hakkındaki görüşünüzü yazınız: ")
    yorumlar.append(yorum)

uzunluklar = [len(y) for y in yorumlar]

iyiSay = 0
for y in yorumlar:
    if "iyi" in y.lower(): 
        iyiSay += 1


en_uzun = max(yorumlar, key=len)
en_kisa = min(yorumlar, key=len)


ortalama = sum(uzunluklar) / len(uzunluklar)

print("\n--- Sonuç ---")
print(f"Toplam yorum sayısı: {len(yorumlar)}")
print(f"\"iyi\" geçen yorum sayısı: {iyiSay}")
print(f"En uzun yorum: {en_uzun}")
print(f"En kısa yorum: {en_kisa}")
print(f"Ortalama uzunluk: {ortalama:.1f} karakter")