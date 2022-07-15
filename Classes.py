#class

#object,instance

from email.headerregistry import Address


class Person:
    pass
#class attribute
    adress="No! information"
#constructer (yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year


#object (instance)
p1=Person("ali",1999)
p2=Person("yağmur",1995)


print(f'name: {p1.name} age: {p1.year} adress:{p1.adress}')
print(f'name: {p2.name} age: {p2.year} adress:{p1.adress}')


# print(type(p1))
# print(type(p2))
