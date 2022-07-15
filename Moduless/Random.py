import random

# result = dir(random)
# result=help(random)

result=random.random()#0.0 - 1.0 arasında bir sayı üretilecektir.
result1=int(random.uniform(10,100))#10 ile 100 arasında sayılar üretilecektir
print(result)
print(result1)

greeting='hello there'
names=["fayik","ecem","ahmet","ecem","demir","mehmet"]
# result=names[random.randint(0,len(names)-1)]
resut=random.choices(greeting)

print(result)