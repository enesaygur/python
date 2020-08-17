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
for say in sayilar:
    if (say%2)!=0:
        print(say," tek olduğu için sayının karesi",say*say)
    else:
        print(f"{say} çifttir ")
