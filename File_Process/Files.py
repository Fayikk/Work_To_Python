# Doya açmak için open() fonksiyonu kullanılır.
#Kullanımı open(dosya_adi,dosya _erişme_modu)
#doya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"w" (Write) yazma modu.Dosyay konumda oluşturur.

# file.close()#açılan dosyanın kapanması gerekir
# file=open("File_Process/newfile.txt","w",encoding='utf-8')
# # file.write("this a try wrting")
# file.close()


#"a" (Append) ekleme.Dosya konumda yoksa oluşturur
# file=open("File_Process/newfile.txt","a",encoding='utf-8')

# metin=input("bir metin giriniz")
# file.write("\n"+metin)

#"x" (create) oluşturma.Dosya zaten varsa hata verir
# file = open("File_Process/newFile1.txt","x",encoding='utf-8')
# file.close()


#"r" (read) okuma.Varsayılan.Dosya konumda yoksa hata verir.


