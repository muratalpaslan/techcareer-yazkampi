# Bu ödev dokümanı, Python'da şimdiye kadar işlenen konuları (Veri Tipleri ve Operatörler)
# pekiştirmek için hazırlanmıştır. Try - catch ya da diğer kontroller es geçilmiştir.

# VERİ TİPLERİ
#1

ad = input('Adınız\n:')
yas = int(input('Yaşınızı Giriniz\n:'))
boy = float(input('Boyunuzu Yazınız\n:'))

print(f"Selam.Benim adım {ad}, {yas} yaşındayım ve boyum {boy} metre")

#2
m = int(input('Matematik notunuzu yazınız\n:'))
f = int(input('Fizik notunuzu yazınız\n:'))
k = int(input('Kimya notunuzu yazınız\n:'))
s = (float(m) + float(f) + float(k))/3

print(f"Matematik,Fizik ve Kimya notlarınızın ortalamasının sonucu budur: {s}")

#3
name = 'İsmail Murat Alpaslan'
print(name[0])
print(name[-1])
print(len(name))
print(name[::-1])
# name.split() ile de mesela bosluklarından ayıabilirim.

#OPERATÖRLER
#4
sayi1 = int(input('İlk sayıyı giriniz\n:'))
sayi2 = int(input('İkinci sayiyi giriniz\n:'))

toplam = sayi1 + sayi2
carpim = sayi1 * sayi2
bolme = sayi1 / sayi2
eksi = sayi1 - sayi2
mod = sayi1 % sayi2

print(f"Verdiğiniz {sayi1} ve {sayi2} sayılarının toplamı: {toplam}\n çarpımı: {carpim}\n bölme sonucu: {bolme}\n çıkarma işlemi sonucu: {eksi}\n ve mod sonucu: {mod}")

#5
ortalama = float(input('Ortalamanızı yazınız\n:'))

if ortalama >= 50 and ortalama <= 100:
    print('Geçtiniz')
elif ortalama < 50 and ortalama >= 0:
    print('Kaldınız')
else:
    print('Lütfen geçerli bir sayı giriniz')

#6
yas = int(input('Yaşınızı giriniz\n:'))

if yas >= 0 and yas < 18:
    print('Ehliyet alamazsınız')
elif yas >= 18 :
    print('Ehliyet alabilirsiniz')
else: 
    print('Lütfen geçerli bir sayı giriniz')

#7
product = float(input('Urunun fiyatını giriniz\n:'))
discoundRate = int(input('İndirim oranını giriniz\n:'))

newPrice = (product * (100 - discoundRate))/100
print(f"Ürününüzün indirimli fiyatı {newPrice}")

#8
yas = 18
ehliyet = True


if yas >= 18 and ehliyet :
    print('Araba kiralayabilirsin')
elif (not yas >= 18) or (not ehliyet): 
    print('Araba kiralayamazsın') 

#Mini Proje
#9
product1 = float(input('Birinci ürünün fiyatını yazınız: '))
product2 = float(input('İkinci ürünün fiyatını yazınız: '))
product3 = float(input('Üçüncü ürünün fiyatını yazınız: '))

total = product1 + product2 + product3

if total > 200 :
    total *= 0.9
    print(f"Toplam fiyatınız 200TL'yi aştığı için %10 indirim uygunlanmıştır. Ödemeniz gereken yeni tutar: {total}")
else:
    print(f"Ödemeniz gereken tutar: {total}")

#10
dYili = int(input('Dogum yilinizi yaziniz: '))
yas = 2025 - dYili 

if yas >= 0 and yas >= 12:
    print('Çocuksunuz')
elif yas >= 13 and yas >= 17:
    print('Ergensiziniz')
elif yas >= 18:
    print('Yetişkinsiniz')

