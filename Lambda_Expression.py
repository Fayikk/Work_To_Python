from tabnanny import check


def square(num):return num**2



numbers=[1,3,5,9]

result=list(map(lambda num: num**2,numbers))
print(result)

# result=map(square,numbers)

# for a in result:
#     print(a)      2.yöntem

# for i in numbers:
    
#    print( square(i)) 1.yöntem


#Enumerate= Her bir elemanın tek tek dolaşılması anlamına gelmektedir.

    
# def check_even(num): return num%2==0
# print(check_even(15))  aynı fonksiyonun kullanımını birde lambda yöntemiyle yapalım

check_even=lambda num: num%2==0

print(check_even(8))


toplama=lambda a,b: a+b#lambda yöntemiyle küçük fonksiyonlar oluşturmak işte bu kadar kolaylar.

print(toplama(15,5))
