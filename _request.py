# import json 
# import requests

# import requests
# import json

# api_url='https://api.exchangerate.host/latest'

# bozulan_doviz=input("Bozulan döviz türü")
# alinan_doviz=input("Alinan döviz türü")
# miktar=int(input(f"ne kadar döviz almak istiyorsunuz.{bozulan_doviz}"))
# result=requests.get(api_url+bozulan_doviz)

# result=json.loads(result.text)

# print("1 {0}={1}  {2} ".format(bozulan_doviz, result["rates"][alinan_doviz],alinan_doviz))
# print("{0} {1}={2}--{} ".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))
