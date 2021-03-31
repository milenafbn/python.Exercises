ano = int(input('Digite um ano: '))
x = ano % 100
y = ano % 400
w = ano % 4
if x == 0:
    if y == 0:
        print('\033[32mÉ um ano bissexto!\033[m')
    else:
        print('\033[31mNão é um ano bissexto!\033[m')
else:
    if w == 0:
        print('\033[32mÉ um ano bissexto!\033[m')
    else:
        print('\033[31mNão é um ano bissexto!\033[m')
#if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0
# tem esse operadores(??) or, and, != (quando vc quer que seja diferente, não == )
