# def square(num): return num**2
# sayilar=[1,3,5,7,9]
# result=square(2)
# print(result)
# karesi=list(map(square,sayilar)) # map dizi içerisindeki her bir elemana ulaşık fonksiyon üzerinden geçirir.
# print(karesi)
# # for döngüsüyle yazdırma
# for item in map(square,sayilar):
#     print(item)
# square=lambda num: num**2
sayilar=[1,3,5,7,9,10,4]
# result=square(3)
# print(result)

def check_even(num):return num%2==0
# result=list(filter(check_even,sayilar))
result=list(filter(lambda num: num%2==0 ,sayilar))
print(result)