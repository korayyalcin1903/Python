para = float(input("Para Miktarınız:"))
faiz = 0.14

birinciYil = para+(para*faiz)
ikinciYil = birinciYil+(birinciYil*faiz)
ucuncuYil = ikinciYil+(ikinciYil*faiz)

print("1. Yıl sonu paranız:",round(birinciYil,2))
print("2. Yıl sonu paranız:",round(ikinciYil,2))
print("3. Yıl sonu paranız:",round(ucuncuYil,2))
