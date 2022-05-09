#print("""
#|||""koray""||
#|||""ragnar""||
#""")

#print("""koray""bey""")


#print(1,2,3,4,5, sep="X")


#print(*"12345")


#print("python\rprogramlama")


#print(3//2)

#saat=10
#dakika=30
#if saat<10 & dakika>10:
#    print("doğru")
#else:
#    print("yanlış")

#a=20
#b=30
#print(a is not b)


#islem = input("+  -  *  /:")
#a,b=3,4
#if islem == "+":
#    print(a+b)
#elif islem=="-":
#    print(a-b)
#elif islem=="*":
#    print(a*b)
#elif islem=="/":
#    print(a/b)
#else:
#    print("hatalı değer girdiniz...")


#liste=["koray","hüseyin","abdulkadir","okan","kutay"]
#h=0
#for i in liste:
#    h+=1
#    print(h,".",i)


#for i in range(0,10):
#    if i==5:
#        pass
#    else:
#        print(i)


#liste=[1,2,"goril","ragnar",2.30]
##print(liste[-2])
#print(liste[len(liste)-1])


#liste = [10,20,30]
#for i in range(0,len(liste)):
#    a=liste[i]
#    a*=2
#    liste.append(a)
#
#for j in range(0,len(liste)):
#    print(liste[j]) 


#liste1=[10,20,30,40,50]
#liste2=liste1[:]
#liste2[1]=15
#print(liste2)


#indis=liste.index(50,2)
#print(indis)

#liste.insert(1,15)
#liste.remove(20)
#del liste[4]
#a=liste.pop(1)
#print(a)
#sonuc = 10 in liste
#print(sonuc)
#print(liste)


liste=[10,3,5,0,1,3,7,10]
#liste.sort()
#for i in range(0,len(liste)):
#    print(liste[i])

#liste.reverse()
#for i in range(0,len(liste)):
#    print(liste[i])
#a=liste.count(10)
#print(a)
toplam=sum(liste)
print(toplam)




#for i in range(1,6):
#    print("*"*i)


#######sayac = 1
#######for i in range(0,6):
#######    for j in range(0,i):
#######        print("*",end="")
#######    print()