#Fonksiyondan fonksiyona döndürme


# def usalma(number):
#     #two= usalma(2) rakamalr bizim taban sayılarımız olacaktır
#     #three= usalma(3)
#     #fonksiyon içerisindeki fonksiyonsa bir değer döndürmek yerine bir fonksiyon döndürdüğümüzü düşünün.

#     def inner(power):
#         return number**power
#     return inner    


# two=usalma(2)
# print(two(3))#power değişken yerinde geçecektir
# three=usalma(3)
# print(three(2))
# # print(three)

# def bolunen(sayi):
#     print("bolunen calist..")
#     def bolen(sayi1):
#         print("Bolen calisti")
#         return sayi/sayi1
#     return bolen    
# result=bolunen(10)
# print(result(2))

# def yetki_sorgula(page):
#     def inner(role):
#         if role =='Admin':
#             return "{0} rolünün {1} sayfasına ulaşabilir ".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz ".format(role,page)

#     return inner
# user1=yetki_sorgula("database management")
# print(user1("Admin"))


# def fabrika(arac):
#     def araba(marka):
#         if marka == 'Wolksvagen':
#             return "{0} aracı {1} nolu fabrikaya giriş yapabilir".format(marka,arac)
#         else:    
#             return "{0} aracı {1} nolu fabrikaya giriş yapamaz".format(marka,arac)

#     return araba

# otomobil=fabrika("Wolksvagen")
# print(otomobil("passat"))

# def islem(islem_adi):
    
#     def toplama(*args):#args sınırsız sayıda argüman almak için kullanılır
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam

#     def carpma(*args):
#         carpim=1
#         for i in args:
#             carpim*=i
#         return carpim
    
#     if islem_adi=="toplama":
#         return toplama

#     else:
#         return carpma

# toplama=islem("toplama")
# print(toplama(1,2,3,4,5,6,7,8,9))

# carpma=islem("carpma")
# print(carpma(1,2,3,4,5,6,7,8,9))
