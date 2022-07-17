with open("File_Process/newfile.txt","r",encoding='UTF-8') as dosya:
    result=dosya.read()
    print(result)
    dosya.seek(20)#cursor'U göndermek istediğimiz indisi seçeriz.
    print(dosya.tell())#yada cursorun o anki byte numarasını öğrenebiliyoruz
    content2=dosya.read()
    print(content2)

#file close işlemini yapmamıza gerek kalmayacaktır.Bu sayede