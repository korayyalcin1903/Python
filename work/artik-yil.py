yil = int(input("bir yıl giriniz:"))

if yil%4==0 and yil%100!=0 or yil%400==0:
    print("artık yıldır...")
else:
    print("artık yıl değildir...")