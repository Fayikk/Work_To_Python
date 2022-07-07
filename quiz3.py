Text1="Bu bir deneme yazısıdır."
Text2="this message for trying"

#text2 karakter dizisinde kaç karakter bulunmaktadır
print(len(Text2))
#text1 karakterinde "bu" karakterlerini alın

print(Text1[2:])
#text2 içerisinden trying karakterini almadan ekrana yazdırım
print(len(Text2))
deneme=Text2.split(" ")
print(len(deneme))
print(deneme[:len(deneme)-1])
#text1 içerisinden ilk 15 ve son 15 karakteri sırasıyla alınız
result=Text1[0:15]
result1=Text1[15:0:-1]#15.indexten -1 indeks azaltarak geriye doğru gitmemiz gerekecektir
#Yani yukarıdaki karakterleri tersten yazdırma işlemi yapmış olduk.
print(result)
print(result1)

deger='12345' * 5
print(deger[25:0:-5])

name,surname,age,job="Emre","Demir",30,"Engineer"

cumle="benim adım "+name+ "soyadım" +surname+" yaşım "+ str(age) +" mesleğim ise" + job
print(cumle)
print("adım {} soyadım {} yaşım {} ve mesleğim {}".format(name,surname,age,job))
#Yukarıdaki gini gerekli atamalr yapılır ve tür dönüşümlerine örnek verileibilir


#abc ifadesini 3 defa yan yana yazdırın
deneme1="abc"
print(deneme1*3)





