#Inheritance(kalıtım): Miras alma

#Person=>name,lastname,age,eat(),run(),drink()
#Student(Person),Teacher(Person)
#Animal=>Dog(Animal),Cat(Animal)



from sre_constants import BRANCH


class Person:
    def __init__ (self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person created")

    def who_am_i(self):
        print("I am a person")  #Kaltıım alan sınıfta bu metoda ulaşım sağalayabilecektir

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)#child sınıf kendine ait bir constructer metod oluştutacaksa eğer kalıtım ile aldığı paren classında constructerını kendi init metodunda belirtmek zorundadır.
        self.number=number
        print("Student crated")
    
    #Overrride işlemi gerçekleştirdik
    def who_am_i(self):
        print("I am a Student")


class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)#Super metodunda self göndermemize gerek yoktur
        self.branch=branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')


p1=Person("Ferhat","Yılmaz")#Her ikisindede init metodu çalışcaktır
s1=Student('Çınar','Turan',190290013)#İnit metodu tetiklenecektir

print(p1.fname+"  "+p1.lname)
print(s1.fname+"  "+s1.lname+"  "+str(s1.number))


p1.who_am_i()
s1.who_am_i()
t1=Teacher("Fayik","Veznedaroglu","Software Engineer")

print(f'Liderimiz {t1.fname} {t1.lname} kendisi {t1.branch} uzmanıdır')