#' Hello world ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin'

result=' Hello world '.strip()#baş ve sondaki boşluk karakterlerini silmeye yarar
result=' Hello world ' .lstrip()#soldaki boşuğu silecektir

#"benim adım fayik" bilgisindeki fayik karakteri hariç diğer biligileri siliniz
cumle="benim adım fayik".strip('benm ad')
print(cumle)

cumle=cumle.count("a")#cümle içerisinde 2 tane 'a' harfi bulunmaktadır

print(cumle)