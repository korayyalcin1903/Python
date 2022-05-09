from xml import dom


mesaj = "koraybey@gmail.com"

#domain = mesaj[9:14]
#print("-----------------")
#yeniMesaj = mesaj[:8]
#
#print(yeniMesaj)
#print(domain)

#print(len(mesaj))
#
#yeniMesaj2 = mesaj[12:len(mesaj)]
#print(yeniMesaj2)

ePosta = "korayyalcin@gmail.com"
domain = ePosta[ePosta.find("@")+1:ePosta.find(".")]
print(domain)