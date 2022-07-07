#tuple tip listeye benzerlik gösterir ancak tam anlamıyla benzerlik göstmezler

list=[1,2,3]
tuple=(1,"iki",3)
print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))
#liste ve tuple'a farklı eleman atamaları yapılabilir
list=("demir","deren")
tuple=("damla","ayşe")
print(list)
print(tuple)
#ancak şunu unutmayın içerik değişim yapmıyormuz.
# list[0]="Ahmet"
# tuple[0]="deniz"
# print(tuple)
#liste ve tuple'lerde farklı olarak listeleerde elemanlar update edilebilirken
#tuple'larda update işlemi yapılamamaktadır.

tuple1=("wolksvagen","opel","ford")
tuple2=("bugatti","lambo","ferrari")+tuple1
print(tuple2)#tuple'larda birleştirme işlemi yapılabilmektedir.
