x,y,z=5,10,20


x,y=y,x
x=x+5
x+=5 #x = x +5
x*=5
x-=5
x/=5
x//=5#burada bölme işleminin tam kısmı ile ilgilenmekteyiz


print(x,y,z)

values= 1,2,3,4,5#bu bizim tuple nesnemizdir.parantez içerisinde yada bu şekilde virgüller ile ayırarak yazılabilir.
x,y,*z=values#aşağıdaki z değerimiz ilk iki karakterden sonraki karakterler için gerekli atamaları yapmıştır.
print(x,y,z)

print(values)
print(type(values))
