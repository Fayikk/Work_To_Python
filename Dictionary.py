# key-value şeklinde çalışmaktadır
#41=>Kocaeli  21=>Diyarbakır

sehirler =["kocaeli","istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli'])

# plakalar={'key':'value' }
plakalar={'diyarbakır':21,'elazığ':23}
print(plakalar['diyarbakır'])

plakalar['elazığ']=21#bu şekilde value değerleri değiştirebilmekteyiz
print(plakalar['elazığ'])

# users = {
#     'fayik':{
#         'age':23,
#         'email':'veznedaroglufayik2@gmail.com'
#     }
#     'bambam'{
#         'age':3,
#         'email':'bambam@hotmail.com'
#     }
# }
# print(users['fayik'],users['bambam'])