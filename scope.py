# name='ENES'
# def ChangeName(new_name):
#     name=new_name
#     print(name)
# ChangeName('Furkan')
# print(name)

###################
x=50
def test():
    global x # dışarıdaki x değerini içeriden etkilemek için global x değerini etkiler.
    print(f'x :{x}')
    
    x=100
    print(f'x değişti :{x}')
    
test()
print(x)