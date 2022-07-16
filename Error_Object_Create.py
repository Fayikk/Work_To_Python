# x=10
# print("Bu bir denemedir")
# if x>5:
#     raise Exception("x 5 den büyük deger alamaz")

# def check_password(psw):
#     import re

#     if len(psw)<8:
#         raise Exception("Parola en az 7 karakter olmalıdır")
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf olmalıdır.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola büyük harf olmalıdır.")
#     elif not re.search("[1-9]",psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[@$]",psw):
#         raise Exception("parola alpha numeric karakter içermelidir")

#     else:
#         print("Geçerli parola girişi sağlandı")    

# password="1234567@1aA"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# finally:
#     print("validation tamamlandı")    


class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name=name
p=Person("Fayikkkkkkk",1998)
