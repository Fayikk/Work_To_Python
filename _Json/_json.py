#db den bilgileri bir android veya web uygulasında taşıyabiliyoruz.
#Cihazlar arasında ortak bir veri türüdür.

import json

person_string='{"name":"Fayik","Languages":["Python","C#"]}'
person_dict={"name":"Fayik","Languages":["Python","C#"]}
# JSON srtring to Dict
# result=json.loads(person)

# result=person["name"][0]

# with open("_Json/person.json") as f:
#     data=json.load(f)
#     print(data["name"])
#     print(data["Languages"])
#     print(data["name"])#Json dosyadı içerisindeki bilgilere bu şekilde ulaşılabilir

# person_dict={
#     "name":"Ali",
#     "Languages":["Python","C#","C++"]
# }
# result=json.dumps(person_dict)#sözlük yapımızı artık string bir bilgiye dönüştürmüş olduk.
# print(result)

# with open("_Json/person.json","w") as f:
#     json.dump(person_dict,f) dosyamızın içerisine ekleme işlemini tamamladık


person_dict=json.loads(person_string)

result=json.dumps(person_dict,indent=4,sort_keys=True)

print(person_dict)
print(result)

