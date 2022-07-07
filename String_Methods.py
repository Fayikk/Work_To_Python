message="Hello There , my name is figoo"
message =message.upper()#btün string büyük harfle yazılırlar
print(message)

message=message.lower()#string ifadeler küçük harf ile yazılırlar
#message.capitalize()=ilk harfi büyük olarak yazdırılır

# message = message.strip()
# print(message)

# message=message.split("*")#her boşluk karakterlerimiz için indeks özellği göreceklerdir.
# # print(message[3])
# message=" ".join(message)

index = message.find("figoo")#figoo'nun ilk harfini arar ve ilk harfinin indeksini ekrana yazdırır
print(index)

boolean=message.startswith("h")#Cümlemiz hangi harf ile başlıyor bunu boolean cinsten döndürmemize yarayacaktır
print(boolean)

message=message.replace('f',"c")#text içerisinde bulduğu karakterlere göre harf değişimşi  yapmaktadır replace metodu.
print(message)

message=message.center(40,"*")
print(message)
#stringler için çok fazla metod mevcuttur eğer istersek w3schoolstan dökümanlara bakabiliriz.
