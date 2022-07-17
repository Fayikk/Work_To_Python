
import re
liste=["1","2","5a","10b","abc","10","50"]

#1:liste elemanları içerisindeki sayısal değerleri bulunuz.
# for a in liste:
#     try:
#         result=int(a)
#         print(result)
         
#     except ValueError:
#         continue



#2:kullanıcı 'q' değeri girmedikçe aldığınız her inputun sayı değeri olduğundan 
#emin olunuz aksi halde hata mesajı yazın.

# while True:
    
#     sayi=input("sayi: ")
#     if sayi=='q':
#         break
#     try:
#         result=float(sayi)
#         print("girilen sayı: {}".format(sayi))
#     except ValueError:
#         print("geçersiz sayı")

#3:Girilen parola içerisinde türkçe karakter mesajı veriniz.





# def Giris(parola):
#     karakterler='şçğüöıİ'
#     for i in parola:
#         if i in karakterler:
#             raise TypeError("Parola türkçe karakter olamaz.")
#         else:
#             pass    
#     print("Başarılı bir parola bilgisi  tanımlandı")

# parola=input("geçerli bir parola giriniz")
# try:
#     Giris(parola)
# except TypeError as err:
#     print(err)    


#4:Faktoriyel fonskiyonu oluşturuop fonksiyona gelen değer için
#hata mesajları verin



# def faktoriyel(sayi):
#     sayac=1
#     while(sayi>0):
#         sayac=sayac*sayi
#         sayi-=1
#     print(sayac)        
# sayi=int(input("faktoriyeli alınacak sayı giriniz:"))

# faktoriyel(sayi)

# if sayi<0:
#     raise ValueError("sayı negatif değerli olamaz")
 

