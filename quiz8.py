csayilar= [1,3,5,7,9,12,19,21]

#1-sayilar listesini while ile ekrana yazdırın
# i=0
# sayac=0
# while(i <= len(sayilar)):
#     print(sayilar[i])
#     i+=1
    
#2-başlangıç ve bitiş değerlerini kullanıcıdan alıp değer aralığını ekrana yazdırınç
# basla=int(input("baslangic degeri giriniz:"))
# bitis=int(input("bitis degerini giriniz: "))

# while(basla<=bitis):
#     print(basla)
#     basla+=1


#3- 1-100 arasındaki sayıları azalan şekilde ekrana yazdırın
# deger=100
# while(deger>=0):
#     print(deger)
#     deger-=1
#4- kullanıcıdan alınan 5 sayıları ekrana sıralı şekilde yazıdırn
# liste=[]
# sayac=0
# while(sayac<5):
    
#     deger=int(input("deger giriniz:"))
#     liste.append(deger)
#     sayac+=1
# liste.sort()
# print(liste)
#6-Kullanıcıdan alacağıız ürün bilgisini sınırsız bir şekilde liste içerisinde saklayacağız
#Ürün sayısını kullanıcıya sorun
#dictionary listesi yapısı(name,price) şeklinde olsun
#ürün ekleme işlemi bittiğinde ürünleri ekranda while döngüsü ile yazdırılsın
urunler=[]

print("Kaç adet ürün eklemesi yapmak istersiniz?")
urun=int(input("giriniz:"))
sayac=0
while(sayac<urun):
    name=input("ürün adı giriniz")
    price=input("fiyat bilgisi giriniz: ")
    urunler.append({"name":name,
                     "price":price })
    sayac+=1

                      
print("calisti")
print(urunler)
print("calisti")
for u in urunler:
     print(f'ürün adi: {u["name"]} ürün fiyati{u["price"]}')
    # f string kullanarak listenin tamamını döndürmeyi sağlıyoruz.