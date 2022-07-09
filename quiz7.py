from datetime import datetime


#1-kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#durumunu kontorl ediniz.Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da 
#üniversite olmalıdır

# print("***EHLİYET ALABİLME KONTROL OTOMASYONU***")
# isim=input("isim giriniz:")
# soyad=input("soyisim giriniz: ")
# yas=int(input("yaş giriniz:"))
# egitim=input("lütfen egitim durumunu giriniz:")

# if yas>=18 and (egitim=="lise" or egitim=="üniversite"):
#     print("ehliyet atlmak için gerekli şartları sağlıyorsunuz")
# else:
#     print("üzgünüz ehliyet için gerekli şartları sağlamıyorsunuz.")
# 2- öğrencinin 2yazılı notlarına ve 1 sözlü notlarına göre
#hesaplama yapın ve karşılık değerini ekrana yazdıran bir prograam yazın.

# sayi1=int(input("1. sınav notlarınızı giriniz:"))
# sayi2=int(input("2. sınav notlarınızı giriniz:"))
# sozlu=int(input("sözlü notunuzu giriniz: "))

# ort=(sayi1+sayi2+sozlu)/3
# if ort<=24:
#     print("not karsiligi 0")
# elif(25<=ort<=44):
#     print("not karsiigi 1")
# elif(45<=ort<=54):
#     print("not karsiligi 2")
# elif(55<=ort<=69):
#     print("not karsiligi 3")
# elif(70<=ort<=84):
#     print("not karsiligi 4")
# elif(85<=ort<=100):
#     print("not karsiligi 5")
# else:
#     print("birşeyler yanlış gitti")        


#3-trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere 
#göre düzenleyiniz
#1.bakım =1.yıl
#2.bakım=2.yıl
#3.bakım=3.yıl
#datetiöme modülünü kullanmamız gerekiyor.
# print("*****ARAÇ MUAYENE OTOMASYONU*****")
# yıl=int(input("yıl bilgisi giriniz: "))
# ay=int(input("ay biligisini girin: "))
# gun=int(input("gun bilgisini giriniz: "))

# Kisiselbilgi=datetime(yıl,ay,gun)
# print(Kisiselbilgi)
# anlık=datetime.now()
# deneme1=anlık-Kisiselbilgi
# print(deneme1)
# print( Kisiselbilgi.year)

# if ((anlık-Kisiselbilgi)>365):
#     print("1 periyodik bakımınız geldi.")
# elif ((anlık-Kisiselbilgi)>(365)*2):
#     print("2.periyodil bakımınız geldi") 
# elif ((anlık-Kisiselbilgi)>(365)*3):
#     print("3.periyodik bakımınız geldi") 
           

