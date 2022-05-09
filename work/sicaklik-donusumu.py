C = int(input("derece cinsinden bir sıcaklık giriniz:"))
F = float(180*C+100*32)/100
K = float(100*F-100*32+273*180)/180

print(F, "Fahrenheit")
print(K, "Kelvin")