import os#os modülü genel olarak işletim sistemi ile alakalı bir bilgi sunmaktadır.
import datetime

#klasorler hakkında bilig sahibi olma vs'de kullanılabilir
# result=dir(os)
# result=os.name
# result=os.getcwd()
# #os.chdir('C:\\') bu metod ile dizin değiştirme işlemlerini gerçekleştirebiliriz
# # os.mkdir("os module")#aynı dizin içersinde adını tanımladığımız klasör oluşacaktır
# print(result)
# result=os.getcwd()

#etkin dizin öğrenme
# print(result)

#oluşturulan klasör içerisine dosya yada farklı uzantılara sahip dosyalar oluşturmaya yarayacaktır.
# os.makedirs("os module\\deneme.txt")


#Listeleme işlemleri
# result=os.listdir()
#örneğin c dizini altında bir listeleme işlemi yapsın
# result=os.listdir('C:\\') C dizini altındaki dosyaları gösteriyor.

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# result=os.stat("Dictionary.py")
# print(result)  Girilen dosya hakkında bilgi verir.

# result=os.stat("Dictionary.py")
# result=result.st_size/1024#Dosya boyunu verir ve byte cinsinden verir.1024 ile çarparak kilobyte cinsinden değerine ulaşabiliriz

#path() uzantılar ile ilgili işlem yapmaktadır.Dosyanın uzantısını değiştirmek veya ismini değiştirmek gibi 
# result=os.path.abspath("Datetime.py") girilen dosyanın konumunu hdd içerisindeki dosya yolunu direk olarak verir

# result=os.path.abspath("C:/Users/fayik/Desktop/Work_To_Python/Datetime.py")Dsoyanın tam yolunu verecektir.

# print(result)


