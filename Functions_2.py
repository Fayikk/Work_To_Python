def sayHello(name="User"):
    print("Hello {}".format(name))
sayHello("Fayik")#Fonksiyon çağırma işlemi bu şekilde gerçekleşir.


def total(num1,num2):
    return num1+num2

result= total(12,21)
print(result)


def yasHesapla(dogumyili):
    return 2022-dogumyili

result1=yasHesapla(1998)    
print(result1)



def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRİNG:Emekliliğe kaç yıl kaldığını belirten bir programdır.
    '''
    yas=yasHesapla(dogumYili)
    emeklilik= 65-yas

    if emeklilik>40:
        print(f'emekliliğinize {emeklilik} yıl kaldı.{isim}')
    else:
        print("Zaten emekli") 

EmekliligeKacYilKaldi(1998,"Mustafa")
EmekliligeKacYilKaldi(1995,"Veysel")
#print(deneme)
    