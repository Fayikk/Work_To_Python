#girilern bir sayının 0-100 arasında olup olmadığını kontrol ediniz
a=int(input("sayi giriniz:"))
result=a>0 and a<100
print(result)
#girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
result1=a>0 and a%2==0
print(result1)
#email ve parola bilgileri ile giriş kontrolü yapınız
email="osman02emre@gmail.com"
password="rambo4455"

email1=input("email giriniz")
password1=input("password giriniz")

result2=email==email1
result3=password==password1
print(result2)
print(result3)
#girilen 3 sayıyı büyüklük olarak karşılaştırınız
a,b,c=int(input())


