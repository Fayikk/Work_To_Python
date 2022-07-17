

#girilen sayılar ile 0'a kadar olan sayıların toplamı 
def recursive_add(sayi):
    if sayi==1:
        return 1

    else:
        return sayi+recursive_add(sayi-1)    


result=recursive_add(5)        
print(result)

#faktoriyel hesabının rekursif çözümü
def faktoriyel(sayi):
    if sayi==1 or sayi==0:
            return 1
    else:
        return sayi*faktoriyel(sayi-1)        

print(faktoriyel(5))


# girilen sayı ile 100 arasındaki sayıların toplamını yazdıran rekurdif ifade
def topla(sayi):
    if sayi==100:
        return 100
    else:
        return sayi+topla(sayi+1)



print(topla(95))
sayi=int(input("1-100 arasında bir sayı giriniz"))

a=1
sayac=0
while sayi<=100:
    sayi+=1
    sayac=sayac+sayi

print(sayac)
