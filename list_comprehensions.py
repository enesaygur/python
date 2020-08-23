# number=[]
# for x in range(10):
#     number.append(x)
# print(number)


################################

# numbers=[x for x in range(10)]     AYNISININ KISA HALİ
# print(numbers)

################################

# numbers=[x*x for x in range(10) if x%3==0] # Karesi alınan sayıların 3 e bölünenleri yazdırıldı 
# print(numbers)


# myString='Hello'
# myList=[]
# #*********************************************************************
# for letter in myString:
#     myList.append(letter)
# print(myList)
# #******************** Üstteki 2 satır kod alttaki 1 satır kod aynı işe yarar ***************
# myList=[letter for letter in myString]
# print(myList)
#************************************************************************

# years=[1996,1987,2000,1994]
# ages=[2020-year for year in years]
# print(ages)

#********************************
# result=[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)
#************************************** AYNI işe yarayan liste yapma yöntemi
# numbers=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
# print(numbers)
#*******************************