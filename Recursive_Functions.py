

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






