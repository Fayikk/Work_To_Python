# def greeting(name):
#     print('hello',name)
# # print(greeting("Fayik"))

# sayHello=greeting

# print(sayHello)
# print(greeting)

# # greeting("ECEM")
# # print(sayHello)

# del sayHello
# # print(sayHello)
# print(greeting)
# def outer(num1):
#     print("Outer calisti")
#     def inner_increment(num1):
#         print("inner calisti")
#         return num1+1
#     num2=inner_increment(num1)    
#     print(num1,num2)
# outer(10)        


#Encapsulation denir(kapsülleme işlemı yapılmıştır.)
# def sayı(sayi1):
#     def topla(sayi1,sayi2):
#         return sayi1+sayi2
#     result=topla(sayi1,10)
#     print(result)    
# sayı(15)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be an integer")
    if not number>=0:
        raise TypeError("Number must be positive")

    def inner_factorial(number):
        if number<=1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)
try:

    print(factorial(5) )       
except Exception as ex:
    print(ex)




