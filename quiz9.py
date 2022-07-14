#1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon yazalım

# def kelimeDöndür(kelime,tur):
#     while tur>=0:
#         print(kelime)
#         tur-=1

# sonuc=kelimeDöndür("fayik",10)        

#2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazalım

# def listeCevir(*liste):
#     liste1=[]
#     for a in liste:
#         liste1.append(a)
#     print(liste1)
# listeCevir("deneme","fayik")

#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun



# def asalsayi(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if(sayi%i==0):
#                     break
#                 else:
#                     print(sayi)


#4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksşyon yazalım


# def tamBolenlerbul(sayi):
#     tamBolenler=[]
#     for i in range(2,sayi):
#         if(sayi%i==0):
            
#             tamBolenler.append(i)
#             print(tamBolenler)        


# deneme=tamBolenlerbul(36)
# print(deneme)