fruits = {'orange','apple','banana'}

#print(fruits[0]) indekslenemez

for i in fruits:

    print(i)

fruits.add('cherry')#ekleme 
fruits.update(['mango','grape'])#ekleme
fruits.remove('mango')#çıkarma 
print(fruits)   
#set'lerde aynı elemandan birden fazla içermez.Update veya append bile eklenirse yine hiçbir değişiklik olmayacaktır
