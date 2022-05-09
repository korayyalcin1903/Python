#sicaklik = 50
#if sicaklik>100 :
#    print("sıcaklık çok yüksek")
#elif sicaklik<0:
#    print("soğuk")
#else:
#    print("ılık")


#sayi = float(input(("bir sayı giriniz:")))
#if sayi>0:
#    print("pozitif")
#elif sayi==0:
#    print("sıfır")
#else:
#    print("negatif")


renk1 = "kırmızı"
renk2 = "beyaz"
renk3 = "yeşil"

secenek1 = str(input("birinci rengi giriniz:"))
secenek2 = str(input("ikinci rengi giriniz:"))

if secenek1 == "kırmızı" and secenek2 == "beyaz" or secenek1 == "beyaz" and secenek2 == "kırmızı":
    print("pembe")
elif secenek1 == "kırmızı" and secenek2 == "yeşil" or secenek1 == "yeşil" and secenek2 == "kırmızı":
    print("mor")
elif secenek1 == "beyaz" and secenek2 == "yeşil" or secenek1 == "yeşil" and secenek2 == "beyaz":
    print("açık yeşil")
else:
    print("hatalı değer girdiniz")