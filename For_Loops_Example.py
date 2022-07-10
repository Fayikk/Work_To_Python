# sayilar = [1,3,5,7,9,12,19,21]

# #1-Sayilar listesindeki hangi sayılar 3'ün katıdır?
# for sayi in sayilar:
#     if sayi%3==0:
#         print("3 ile tam bölünür: "+ str(sayi))


# #2-Sayilar listesindeki sayıların toplamı kaçtır?
# toplam=0
# for sayi1 in sayilar:
#     toplam=toplam+sayi1
# print(toplam)
# #3-Sayilar listesindeki tek sayıların karesini alınız. 
# toplam1=0
# for sayi2 in sayilar:
#     if sayi2%2!=0:
#         print("sayi tektir: "+ str(sayi2))
#         toplam1=toplam1+sayi2
# print(toplam1)        


# sehirler = {"kocaeli","istanbul","ankara","izmir","rize"}
# #4- Şehirlerden hangileri en fazla 5 karakterlidir?

# for sehir in sehirler:
#     if len(sehir)>5:
#         print(sehir)



urunler=[
    {"name":"samsungs6","price":"3000"},
    {"name":"samsungs7","price":"4000"},
    {"name":"samsungs8","price":"5000"},
    {"name":"samsungs9","price":"6000"},
    {"name":"samsungs10","price":"7000"}
           ]
#5-Ürünlerin fiyatları toplamı nedir?

# toplam=0
# for urun in urunler:
#     print(urun['price'])
#     toplam=toplam+int(urun["price"])
# print(str(toplam))

#6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz:
for urun1 in urunler:
    if urun1["price"]>="5000":
        print(urun1["name"])




