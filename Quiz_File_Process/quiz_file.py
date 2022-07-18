# with open("Quiz_File_Process/file.txt","a+") as file:
#     pass
#uygulamada
#kullanıcıdan ad,soyad ve 3 not istenecektir.Bu bilgileri bir dosyaya kaydedeceğiz
#kaydedilen dosyadan ortalamları çekerek.Kulanıcıların harf karşılıklarını ona geri yansıtacağız
#istendiği zamanda hesaplanan değerlerin hepsini bir dosyaya kaydedebileceğiz
# 
# while karakter=='y':
karakter=input("ogrenci işlemlerine devam etmek istermisin?(y/n)")
id=1
while karakter=='y':
    karakter=input("ogrenci işlemlerine devam etmek istermisin?(y/n)")
    if karakter=='n':
        break
    ad=input("İsim giriniz")
    soyad=input("Soyisim giriniz")

    not1=int(input("birinci notu giriniz"))
    not2=int(input("ikinci notu giriniz"))
    not3=int(input("üçüncü notu giriniz"))

    ortalama=(not1+not2+not3)/3
        # harf_karsiligi=""
        # if ortalama>0 and ortalama<49:
        #     harf_karsiligi="FF"
        # elif ortalama>49 and ortalama<69:
        #     harf_karsiligi="CD"
        # elif ortalama>69 and ortalama<89:
        #     harf_karsiligi="BB"
        # elif ortalama>89 and ortalama<=100:
        #     harf_karsiligi="AA"
        # else:
        #     print("girilen değerlerin harf karşılıkları bulunamadı")
        # " Ortalama= "+str(ortalama)+" Harf Karsiligi: "+harf_karsiligi+
        
    with open("Quiz_File_Process/Ogrenciler.txt","a+",encoding='utf-8') as file:
        file.write(str(id)+"-"+ad+" "+soyad+"--"+"  Ogrencinin Not bilgileri: "+str(not1)+"-"+str(not2)+"-"+str(not3)+"\n")
        id+=1
    

with open("Quiz_File_Process/Ogrenciler.txt","r") as file:
    satir=file.readlines()   
    for i in satir:
        
        print(i)
        





