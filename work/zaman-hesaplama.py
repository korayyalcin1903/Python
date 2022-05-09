gun = int(input("kaç gün:"))
saat = int(input("kaç saat:"))
dakika = int(input("kaç dakika:"))
saniye = int(input("kaç saniye:"))

toplamSaniye = (gun*24*60*60)+(saat*60*60)+(dakika*60)+saniye
print("toplam saniye = ",toplamSaniye)