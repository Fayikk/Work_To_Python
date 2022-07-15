#Classlar içerisinde metofd  oluşturmak


class person:
    address='No! information'

    def __init__(self,name,surname,year):
        self.name=name
        self.surname=surname
        self.year=year

    #Instance method oluşturalım
    def Intro(self):#Fonksiyonların ,metodlar içi dolu bu şekilde oluşturualbiliyorlar.
        print('Hello there '+ self.name)

    def CalculateAge(self):
        return 2022 - self.year    


    # def deneme(self):#Ne olursa olsun metodları self ile doyurmamız gerekmektedir.
    #     print("Bu bir denemedir")    


p1=person("Fayik","Veznedaroglu",1998)
p2=person("Mustafa","Veznedaroglu",1965)


p1.Intro()
p2.Intro()

# p1.deneme()

print({"adi: {} ,soyadi: {}, dogum yili:{}".format(p1.name,p1.surname,p1.year)})
print({"adi: {} ,soyadi: {}, dogum yili:{}".format(p2.name,p2.surname,p2.year)})

print(f"Benim yaşım: {p1.CalculateAge()} ")
print(f"Benim yaşım: {p2.CalculateAge()} ")

class Circle:
    pi=3.14#Class seviyesinde dtanımlama işlemi yapıldı.

    def __init__(self,yaricap=1):
            self.yaricap=yaricap

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def Alan_Hesapla(self):

        return self.pi *(self.yaricap*self.yaricap)      

c1=Circle()# eğer istersek yarıçap bilgisini bildirebiliriz.Atama yapılmazsa default olarak 1 değeri yarıçap değerine atanacaktır.
c1.yaricap=5
Alanı=c1.Alan_Hesapla()
Cevresi=c1.cevre_hesapla()
print(Alanı)
print(Cevresi)
