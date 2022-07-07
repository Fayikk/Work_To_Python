from tkinter import Y


x=5
y=25

x=y
y=20
print(x,y)#int,bool,float,string bunlar değer tiplerdir
#x'in değeri 25 kalırken y'nin değeri son değer atamsından gelen 20 değeri olacaktır


#reference types=>list,class,new etc.
#referans tipler bellekte tuttukları yeri aldıkları için bunu etkilemektedir.
a=["apple","banana"]
b=["apple","banana"]

a=b
b[0]="grape"
print(a ,b)