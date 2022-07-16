#error handling


# try:#hata gelebilecek kod bloklarını try içerisine alıyoruz
#     x=int(input('x:  '))
#     y=int(input('y:  '))
#     print(x/y)
# except ZeroDivisionError:
#     print("Y için 0 girilemez")
# except ValueError as deger_hatasi:
#     print("yanlış deger girdiniz")

# try:
#     x=int(input('x:  '))
#     y=int(input('y:  '))
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")

# try:
#     x=int(input('x:  '))
#     y=int(input('y:  '))
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")
# else:
#     print("Herşey yolunda")

# while True:

#     try:
#         x=int(input('x:  '))
#         y=int(input('y:  '))
#         print(x/y)
#     except Exception as ex:
#         print("yanlış bilgi girdiniz", ex)
#     else:
#         break #else bloğuna geldikten sonra döngü dışarısına çıkacaktır.
#     finally:#Kaynakların kapatılması gerekmektedir
#         print("try except sonlandı")

