sayilar=[1,3,5,7,9,12,19,21]
# Hangi sayılar 3'ün katıdır?##############################################
# for say in sayilar:
#     if say%3==0:
#         print(f"{say} Sayısı 3'ün katıdır.")
#     else:
#         print(f"{say} sayısı 3'ün katı değildir.")
# 
# sayilar listesindeki sayıların toplamı kaçtır?########################
# top=0
# for say in sayilar:
#     top=top+say
# print(top)  
#
# sayilar listesindeki tek sayıların karesini alınız? ####################
# for say in sayilar:
#     if (say%2)!=0:
#         print(say," tek olduğu için sayının karesi",say*say)
#     else:
#         print(f"{say} çifttir ")
##############################################################################
sehirler=['kocaeli','istanbul','ankara','izmir','rize']
# Şehirlerden hangisi en fazla 5 karakterlidir?
# for sehir in sehirler:
#     if len(sehir)<=5:
#         print(sehir)
#     else:
#         print(f"{sehir} -Karakter sayısı 5 ten fazladır ")
#
urunler = [
{'name':'samsung s6','price':'3000'},
{'name':'samsung s7','price':'4000'},
{'name':'samsung s8','price':'5000'},
{'name':'samsung s9','price':'6000'},
{'name':'samsung s10','price':'7000'}
          ]
###################################### toplam fiyatı bul
# toplam=0
# for urun in urunler:
#     fiyat=int(urun['price'])
#     print(fiyat)
#     toplam+=fiyat
# print("toplam ürün fiyatı =",toplam)

# fiyatı 5000 ve altı olan ürünler hangileridir? ######################3

for urun in urunler:
    if int(urun['price'])<5000:
        print(f"{urun['name']} fiyatı {urun['price']}")