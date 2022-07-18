#Decorator
#decorator fonksiiyonlat vir fonksiyona bir özellik eklemek istediğimiz zaman bize yarar sağlıyor
#oluşturulandecorator fonksiyonu bir çok yerde kullanıp özelleştirebiliyoruz.

# def my_decorator(func):
#     print("fonksiyon tetiklendi")
#     def wrapper(name):
#         print("fonksiyondan önce olan işlmeler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return  wrapper
# def SayHello():#sayhello fonksiyonunu çağırdığımız zaman dolaylı olarak my_decorator fonksiyonuuda tetiklemiş olmamız gerekecektir
#     print("hello,Ana fonksiyonumuz tetikleyen fonksiyonun statementtaki işlemleri")    
# def Saygreeting():
#     print("greeting")

# SayHello=my_decorator(SayHello)
# Saygreeting=my_decorator(Saygreeting)

# SayHello()
# print("***********************")
# Saygreeting()

# def matematik(sayi1):
#     print("tetikleme gerceklesti")
#     def anadal(sayi2):
#         return sayi1+sayi2
#     return anadal    
# # result=matematik(1)
# print(result(3))

# def my_decorator(func):
#     print("fonksiyon tetiklendi")
#     def wrapper(name):
#         print("fonksiyondan önce olan işlmeler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return  wrapper

# @my_decorator
# def Sayhello(name):
#     print("Heloo",name)#burada biraz evvel yapıalan decorator işlemlerinin daha pratik bir yolu gösterilmiştir.

# Sayhello("Fayik")

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("süresi: "+str(finish-start))
    return inner
#decorator fonksiyon kullanarak kod tekrarının önüne geçmiş olduk.hem zamandan hemde alandan tasarruf edip daha kurumsal denilebilecek bir yapı ortaya çıkardık.

@calculate_time
def usalma(a,b):
    
    print(math.pow(a,b))

@calculate_time    
def faktoriyel(num):
    
    print(math.factorial(num))

@calculate_time    
def toplama(a,b):
    return a+b

usalma(2,3)
faktoriyel(3)
toplama(6,6)


