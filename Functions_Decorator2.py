import math
import random
def islem(func):
    print("decorator tetiklendi")
    def uret(*args,**kwargs):
        deger=random.randint(1,100)
        func(*args,**kwargs)
        print("kompleks işlemin sonucu: "+str(deger))
    return uret
@islem
def usalma(sayi1,sayi2):
    print(math.pow(sayi1,sayi2))

usalma(2,3)