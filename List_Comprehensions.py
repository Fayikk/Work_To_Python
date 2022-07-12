# #For ve while döngüsüne alternatif
# numbers= []
# for x in range(10):

#     numbers.append(x)
#     print(numbers)

# numbers=[x for x in range(10)]
# print(numbers)    

# numbers = [x*x for x in range(10)  if x%3==0]
# print(numbers)

# MyString="Hello"
# mylist=[]

# for letter in MyString:
#     mylist.append(letter)

# mylist=[letter for letter in MyString]

# print(mylist)

# years=[1998,1999,2000,2001,2002,2003]
# ages=[2022-year for year in years]
# # yapmak istenen işlem-> döngü devamı
# print(ages)




# result=[x if x%2==0  else "tek" for x in range(5,100,5)]
# print(result)

# deneme=[a if a%3==0   else "3e bölünemez" for a in range(1,10)]
# print(deneme)

#bir şekilde atama yapılmaktadır
result =[]

for x in range(4):
    for y in range(3):
        result.append((x,y))
        print(x,y)      
#yukarıdaki örneğin farklı bir tür örneği yapılmaktadır.
numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)
  
