# liste=[1,2,3,4,5]

# iterator=iter(liste)

# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))   
# # print(next(iterator))

# for i in liste:
#     print(i)

# iterator=iter(liste)
# while True:
#     try:
#         element=next(iterator)
#         print(element)
#     except StopIteration:
#         break    

class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

