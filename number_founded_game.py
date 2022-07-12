import random

#1-100 arasında rastgele üretiecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın
#random modülü kullanılacaktır
#100 üzerinden puanlama yapıalacaktır.Her soru 20 puan.
#hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın


deger=random.randint(1,10)
hak=int(input("KAÇ HAKKINIZ OLSUN İSTERSİNİZ?"))
puan=100

oyna=int(input("sayi icin bir tahmin yap:"))
sayac=1
while sayac<=hak:
    sayac+=1
    
    if deger>oyna:
        print("Yukari: ")
        oyna=int(input("deger girin:"))
    elif deger<oyna:
        print("asagi")
        oyna=int(input("deger giriniz: "))
    elif deger== oyna:
        print("bravo! girilen sayıyı doğru buldun")    
        print("sayi: "+str(deger))
        print("Puanın: {}".format(puan))
    else:
        print("Birşeyler hatali olmali")
    puan=puan-(puan/hak)
