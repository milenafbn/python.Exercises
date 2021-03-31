n = int(input('Digite um número: '))
som = 0
for x in range(1,n+1):
    if n % x == 0:
        print('\033[32m',end='')
        som += 1
    else:
        print('\033[31m',end='')
    print(f'{x}',end=' ')
if som == 2:
    print('\n\033[37mé primo!\033[m')
else:
    print(f'\n\033[37mnão é primo\033[m')
