## Bir öğrencinin 2 sınav ve 1 sözlü notunun ortalamasını bulup not karşılığını yazdırmak
sinav1=int(input("Sınav Notu 1 :"))
sinav2=int(input("Sınav Notu 2 :"))
sozlu=int(input("Sözlü Notu :"))
sonuc=int((sinav1+sinav2+sozlu)/3)
if sonuc>=0 and sonuc<=24:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 0')
elif sonuc>=25 and sonuc<=44:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 1')
elif sonuc>=45 and sonuc<=54:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 2')
elif sonuc>=55 and sonuc<=69:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 3')
elif sonuc>=70 and sonuc<=84:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 4')
elif sonuc>=85 and sonuc<=100:
    print(f'Sınav ortalamanız {sonuc} olduğundan not karşılığınız 5')
else:
    print('Sınav notunuz hesaplanamadı.')