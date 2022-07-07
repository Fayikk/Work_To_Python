#"bmw,mercedes,opel,mazda" elemanlarına sahip bir liste oluşturunuz
'''
1-liste kaç elemanlıdır
2-listenin ilk ve son elemanı nedir
3-mazda degerini,toyota ile degistirin
4-mercedes listenin bir elemanımıdır
5-listenin -2 indeks degeri nedir
6-listenin ilk 3 elemanını alın
7-listenin son 2 elemanları yerine toyota ve renault degerelrini ekleyin
8-listenin üzerine audi ve nissan degerlerini ekleyin
9-listenin son elemanını silin
10-listenin elemanlarını tersten yazdırın

''' 

from msilib.schema import ListView


liste=["bmw","mercedes","opel","mazda"]
# print(len(liste))#1
# print(liste[0],liste[len(liste)-1])#2
# liste[3]="toyota"
# print(liste)#3
# boolean=liste[2]
# boolean="mercedes"
# print(boolean)#4
# print(liste[-2])#5
# print(liste[:3:1])#6
# liste[len(liste)-1]="Toyota"
# liste[len(liste)-2]="Renault"
# print(liste)#7
liste.remove("bmw")
print(liste)
liste.append("audi")
liste.append("Niisan")
liste.append("bmw")
print(liste)#8

liste.remove(liste[len(liste)-1])
print(liste)#10

