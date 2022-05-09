a = int(input("Bir sayı giriniz:"))
b = int(input("Bir sayı giriniz:"))

carpim = float(a*b)
bolum = float(a/b)
kalan = float(a%b)
ussu = float(a**b)

print(a,"X",b,"=",int(carpim))
print(a,"/",b,"=",round(bolum,2))
print(a," mod ",b,"=",round(kalan,2))
print(a,"^",b,"=",int(ussu))