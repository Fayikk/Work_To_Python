#Generatorlarda amacımız bellek üzerinde yer tutmayan bir yapı oluşturmaktır.

def cube():
    

    for i in range(50000):
        yield i ** 3 


generator=cube()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))eleman sayısını aşar hata alırız




