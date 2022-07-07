#kullanıcının brüt maaşından net maaşını bulan bir program yazalım

maasAli = 5000
maasAhmet= 4000
vergi=0.27

maas=maasAli-(maasAli*vergi)
print(maas)
#Değişken tanımlama kuralları
#diez işareti ile python da yorum satırına alabiliriz

#değişken belirlerken bazı kurallarımız vardır.
#değişkenler sayı ile başlayamaz
#değişkenleri tanımladığımız anda içerisine bir değişken ataması yapmamaız gerekmektedir.
number1=10
number1 +=30
print(number1)
#değişken tanımlarken büyük-küçük harf duyarlılığı vardır.
age = 20
AGE = 30
#string ifadeler aşağıdaki gibi kullanılırlar
name="Fayik"  #string ifadedir
İsStudent=True # boolean ifadedir.
print(age)
print(AGE)
_a="10"
b="30"
print(_a+b)#cevap olarak string değer atadığımızadn 1030 diye bir çıktı alacağız.

FirstName="Fayik"
LastName="Veznedaroglu"
print(FirstName+LastName)

x,y,İsStudent=(1,3,False)#şeklinde değer atamalarımızı yapabiliriz
print(x)

