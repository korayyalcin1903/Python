sesli = ["a","e","ı","i","o","ö","u","ü"]
harf = (input("harf giriniz:"))

for i in range(7):
    if sesli[i] in harf:
        print("Girdiğiniz harf seslidir...")
        break
    else:
        print("Girdiğiniz harf sessizdir...")
        break