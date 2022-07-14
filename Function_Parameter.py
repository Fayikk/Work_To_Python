# # def changeName(n):
# #     n='ada'


# # name='yiğit'

# # changeName(name)

# # def change(n):
# #     n[0]="İstanbul"

# # sehirler=["Ankara","İzmir"]
# # n=sehirler[:]#değer tipe döndürülen sehirler listesi slizing ile değer tip işlemlerine dönüştürüülüp değer döndürme işlemi gerçekleşmezler

# # change(sehirler[:])

# # n[0]="İstanbul"
# # print(sehirler)




# # change(sehirler)
# # print(sehirler)

# # def add(*params): Tek yıldız ifadesi ile tuple oluşturmuş oluyoruz
# #     print(type(params))
# #     sum=0
# #     for n in params:
# #         sum=sum+n
# #     return sum

# # print(add(12,21,5))    
# # print(add(12,2))    

# def displayUser(**args):#Burada ** (iki yıldız) kullanımı dictionary kavramnı bizim çağıracaktır.
#     print(type(args))
    
#     for key,value in args.items():
#         print('{},{}'.format(key,value))


# displayUser(name= 'Cinar',age =2,City='İstanbul')
# displayUser(name= 'Cinar',age =2,City='İstanbul',phone='1234')
# displayUser(name= 'Cinar',age =2,City='İstanbul',phone='1234',email='asas')

# def myfunc(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
# result=myfunc(10,20,30,40,50,60,isim="Fayik",departman="Software engineer")
# print(result)