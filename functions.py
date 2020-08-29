# def sayHello(name="Misafir"):
#     return(f"Hello {name}")

# msg=sayHello("Enes")
# print(msg)

# def total(num1, num2):
#     return num1+num2
# result=total(2,4)
# print(result)

# def yasHesapla(dogumyili):
#     return 2020-dogumyili
# yas=yasHesapla(1996)
# print(yas)

# def emeklilikKacYilKaldi(dogumYili, isim):
#     '''
#     DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
#     INPUT:Dogum yili
#     OUTPUT:Hesaplanan yil bilgisi
#     '''
#     yas=yasHesapla(dogumYili)
#     emeklilik=65-yas
#     if emeklilik>0:
#         print(f"Emekliliğinize {emeklilik} yıl kaldı")
#     else:
#         print("Zaten emekli oldunuz.")
# emeklilikKacYilKaldi(1996,"Enes")
# emeklilikKacYilKaldi(1949,"Veli")
# print(help(emeklilikKacYilKaldi))

# def ChangeName(n):
#     n='ada'
# name='Enes'
# ChangeName(name)
# print(name)


# def change(n):
#     n[0]='İstanbul'
# sehirler=['Ankara','İzmir']
# change(sehirler[0:2])

# print(sehirler)

# def add(*params): # Tuple listesi şeklinde olur tek * olursa
#    print(type(params))
#     return sum((params))
# print(add(10,20,15))
# print(add(10,20,15,23,22))

# def displayUser(**args): # 2 adet ** dictionary olması demektir.
#     print(type(args))
#     for key,value in args.items():
#         print('{} is {} '.format(key,value))
# displayUser(name='Enes', age=2, city='İstanbul')
# displayUser(name='Burak', age=2, city='Ankara')
# displayUser(name='Furkan', age=2, city='Bursa')
