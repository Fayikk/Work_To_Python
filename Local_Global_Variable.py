# #Global scope
# x= 'global x'
# def function(x):
#     #Local scope
#     x='local x'


# print(function(x))
# print(x)    


# name = "Çınar"
# def changename(new_name):
#     name = new_name
#     print(name)


# print(changename("ada"))
# print(name)    

##############3

# name="global string"

# def greeting(name):
#     name="Fayik"

#     def hello():
#         print("hello"+name)
#     hello()    

# print(name)
# greeting(name)

x= 50
def test():
    global x#Dışarıdaki x bilgisini global olarak fonksiyon içerisine tanımladığımız için x üzerinde yapılan her işlem 'x' gloablde etkilenmesine neden olmaktadır.
    print("x"+ str(x))
    x=100
    print("changed x to  "+str(x))

test()    

# print(x) Global olarak tanımlanmış x bilgisini bize verecektir.
print(x)