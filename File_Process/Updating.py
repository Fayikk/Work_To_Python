# with open("File_Process/newfile.txt","r+",encoding='utf-8') as file:#r+ hem okuma hemde yazma işlemlerini gerçekleştirir
#     file.seek(20)#20.byte'tan itibaern değiştirme işlemini gerçekleştirdi 
#     file.write("Deneme")


# with open("File_Process/newfile.txt","r+",encoding='utf-8') as file:#r+ hem okuma hemde yazma işlemlerini gerçekleştirir
    
#     print(file.read())#satır satır okuma işlemini gerçekleştirir



#Sayfa sonuna append yapma işlemi.
# with open("File_Process/newfile.txt","a",encoding='utf-8') as file:#"a" ile açılan dosyalarda txt en sondaki dolu satırdan hemen bir sonraki boş satırda ekleme işlemi yapar(append)
#     file.write("\nbu içerik sayfanın sonuna gelmelidir.")

# with open("File_Process/newfile.txt","r+",encoding='utf-8') as file:#r+ hem okuma hemde yazma işlemlerini gerçekleştirir
    
#     print(file.read())#satır satır okuma işlemini gerçekleştirir

#**** Sayfa ortasında güncelleme işlemi****

# with open("File_Process/newfile.txt","r+",encoding='utf-8') as file:
#     list=file.readlines()
#     list.insert(1,"Ferhat Yılmaz\n")
#     file.seek(0)
#     file.writelines(list)#writeline satırları okumamıza yardımcı olur.
# with open("File_Process/newfile.txt","r+",encoding='utf-8') as file:#r+ hem okuma hemde yazma işlemlerini gerçekleştirir
    
#      print(file.read())    



