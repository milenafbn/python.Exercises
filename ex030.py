print('Par ou Ímpar?')
x = int(input('Digite um número: '))
r = x % 2
if r == 0:
    print('\033[34mÉ par!\033[m')
else:
    print('\033[34mÉ ímpar!\033[m')



'''n = len(x) - 1
b = x[n]
if b == '0':
    print('É par!')
if b == '2':
    print('É par!')
if b == '4':
    print('É par!')
if b == '6':
    print('É par!')
if b == '8':
    print('É par!')

else:
    print('É ímpar!')'''
