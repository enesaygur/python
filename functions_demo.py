    #1 Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon
# def yazdir(kelime,adet):
#     print(kelime * adet)
# yazdir("Enes\n", 5)

    #2 Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ekleyen fonksiyon
# def listeyeCevir(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
#     return liste

# result=listeyeCevir(10,20,30,'Merhaba')
# print(result)

    #3 Gönderilen 2 sayı arasındaki asal sayıları bulun.

# def asaySayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi >1:
#             for i in range(2,sayi):
#                 if sayi % i ==0:
#                     break
#             else:
#                 print(sayi) 
# sayi1=int(input("Sayı 1:"))
# sayi2=int(input("Sayı 2:"))
# asaySayilariBul(sayi1,sayi2)

    #4 Kendisine gönderilen bir sayının tam bölenlerini liste şeklinde yazıdırın.
def tamBolenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if (sayi % i ==0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))
 
