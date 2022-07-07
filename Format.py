name="Fayik"
surname="Veznedaroglu"
age=23
print("My name is {}, surname is {}".format(name ,surname))
print("My name is {n}, surname is {s}".format(n=name ,s=surname))

result= 500/780
#aşağıdaki yapıda tamsayı dahil virgülden sonra 3 hane ekrana yazdıracaktır.
print("Resul is : {r:1.3}".format(r=result))

#f string kullanımı aşağıdaki şekildeki gibi kullanılmaktadır.
print(f"My name is {name}, surname is {surname} age {age}".format(name ,surname))
