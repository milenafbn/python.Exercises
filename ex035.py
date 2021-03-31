a = float(input('tamanho da primeira reta: '))
b = float(input('tamanho da segunda reta: '))
c = float(input('tamanho da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[7;32;40mForma um triângulo!\033[m')
else:
    print('\033[7;31;40mNão forma um triângulo!\033[m')