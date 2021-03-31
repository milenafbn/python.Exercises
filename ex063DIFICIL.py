print('-'*24)
print(' Sequência de fibonacci')
print('-'*24)
a = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('0 > 1 > ',end='')
while cont <= a:
    t3 = t1 + t2
    print(f'{t3} > ',end='')
    t1 = t2
    t2 = t3
    cont += 1
print('fim')