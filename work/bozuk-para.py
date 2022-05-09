para = float(input("Para:"))

bolum = int(para/1)

kalan = float(para%1)

kalaninBolumu = float(kalan/10)

if 0.99>=kalan>=0.5:
    print(bolum," tane 1TL","1 tane 50KR")
elif 0.5>kalan>=0.25:
    print(bolum," tane 1TL","1 tane 25KR")
elif 0.25>kalan>=0.10:
    print(bolum," tane 1TL""1 tane 10KR")
elif 0.10>kalan>=0.05:
    print(bolum," tane 1TL","1 tane 5KR")
else:
    print(bolum," tane 1TL","1 tane 1KR")


print("bölüm:",bolum," kalan:",kalan," en son:",kalaninBolumu)

        
