# name =''
# while not name.strip(): # .strip() metodu baştaki boşluğu silmek için
#     name=input("İsminizi giriniz ... :")
# print(f"Merhaba {name}")
        # 1- 100 arası sayıları yazdırma
# x=1
# while x<=100:
#     print(x)
#     x+=1

# 100 den küçük girilen sayının tek mi çift mi olduğunu bulmak.
# x=0
# while x<5:
#     sayi=int(input("Sayı giriniz:"))
#     if sayi % 2== 0:
#         print(f'{sayi} çifttir ')
#     else:
#         print(f'{sayi} tektir ')
#     x+=1
# print("Bitti..")

#############################################################################################
sayilar=[1,3,5,7,9,12,19,21]
#1 Sayılar listesini while ile ekrana yazdırma

# x=0
# while x<len(sayilar):
#     print(sayilar[x])
#     x+=1

#2 Başlangıç ve bitiş değerlerini kullanıcıdan girip aradaki tüm tek sayıları ekrana yazdırın

# x=int(input("Başlagıç sayısını giriniz."))
# y=int(input("Bitiş sayısını giriniz."))
# while x<=y:
#     if x%2==1:
#         print(f"{x} sayısı tektir")
#     x+=1

#3 1-100 arası sayıları azalan sırada yazdırın.

# x=100
# while x>=1:
#     print(x)
#     x-=1

#4 Kullanıcının girdiği 5 sayıyı  sıralı şekilde yazdırın

# numbers=[]
# i=0
# while i<5:
#     sayi=int(input("Sayı giriniz.:"))
#     numbers.append(sayi) 
#     i+=1
# numbers.sort(reverse=True) # sort methodu sıralar içine reverse=true yazılırsa tersi 
# #şeklinde sıralamyı yapar.
# print(numbers, " Ters")
# numbers.sort()
# print(numbers," Normal")
