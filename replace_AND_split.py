#replace
mesaj = "Merhaba Dünya"
#mesaj = mesaj.replace("ü","u")
print(mesaj.replace("ü","u"))
print(mesaj)

print(mesaj.replace("a","e"))

#split ---- Dizi haline getirmek
bilgi = "Koray Yalçın 34 İstanbul ".strip()  #strip boşluk atmak için kullanılır
print(bilgi.split())
print(bilgi.split(" "))
print("Soyadı = " + bilgi.split(" ")[1])