import re
# result=dir(re)
#regular expression
#mail adresi formata uygunumudur yoksa değilmidir tarzında uyarıları verebilir.
#yada sayısal değerler girilmesini beklerken kullanıcı farklı bir karakter girerse gibi.


cumle="Unity kursu: Unity Oyun programlama kursu"
#re.findall()

# result=re.findall("Unity",str) girilen ifadenin,başlığımız içerisinde kaç tane olduğunu bulur.

# result=re.split("U",str) #kaç boşluk olduğunu söyleyen programdır result=re.split("U",str) split ile U karakteri ile ilgili genel işlemleri yapmamızı sağlar.Split ayırma metodudur.
# result=re.sub(" ","-",cumle)#sub substring metodunu kısaltılmış halidir.Substring metodu ise verilen karakterlerin isetenen şekilde değiştirilmesi sağlamaktadır.
#Yukarıda boşluk karakterlerinin yerine '-' işareti koyuldu

# result=re.search("Unity",cumle)

# result=re.findall("..",cumle) İki basamaklı olan karakterlerin ekranda yazdırılmasını sağladı.

# result=re.findall("U...y",cumle)

##  "^" bu işarete carrot işareti denmektedir.


# result=re.findall("^U",cumle) U ile başlayan bir ifadenin olduğunu bana söylemektedir.

# print(result)

