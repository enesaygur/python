## Ehliyet alma durumu yaş en az 18 ve eğitim lise veya üniversite olmalıdır.
isim= input('İsim :')
yas=int(input('Yaşınız :'))
egitim=input("Eğitim durumu :")

if yas <18:
    print(f'Yaş :{yas} ✖')
else :
     print(f'Yaş :{yas} ✔')

if egitim == 'üniversite' or egitim=='lise' :
    print(f"Eğitim : {egitim} ✔ ")
else :
    print(f"Eğitim : {egitim} ✖ ")
if yas>=18 and (egitim=='üniversite' or egitim=='lise'):
    print(f'{isim} adlı kişi ehliyet almaya uygundur')
else:
    print(f"{isim} adlı kişi ehliyet almaya uygun değildir.") 
##  ✔    ✖