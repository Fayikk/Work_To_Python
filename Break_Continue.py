name="Fayik veznedaroglu"

for letter in name:
    
    if letter=="a":
        continue#Continue ifademizde döngü "a" harfine geldiği zaman burayı görmezden gelip devam etme işlemi yapacaktır.
    print(letter)

x=0

while x<5:
    if x==2:
        break#breakkomutunda belirlen koşuldan sonra var olduğu bloğun içerisinden çıkış sağlayacaktır.
    print(x)
    x+=1    



#1-100 kadar olan tek sayıların toplamı
    
a=0
sayac=0
while a<=100:
    a+=1
    if a%2==0:
        continue
    sayac=sayac+a
    

print(sayac)        