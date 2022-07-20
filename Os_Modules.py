import os#os modülü genel olarak işletim sistemi ile alakalı bir bilgi sunmaktadır.
#klasorler hakkında bilig sahibi olma vs'de kullanılabilir
result=dir(os)
result=os.name
result=os.getcwd()

os.mkdir("os module")#aynı dizin içersinde adını tanımladığımız klasör oluşacaktır
print(result)