import random
sayi=random.randint(1,10)

hak=5
sayac=0
while hak > 0:
    hak-=1 
    sayac+=1
    tahmin=int(input("Tamininiz:"))
    if tahmin==sayi:
       
        print(f"Tebrikler {sayac}. Denemenizde Bildiniz")
        break
    elif sayi>tahmin:
        print("Yukarı")
    else:
        print("Aşağı")
    
    print(f'Kalan hakkınız:{hak}')
    if hak==0:
        print(f"Hakkınız Bitti.. Sayı :{sayi}")
        