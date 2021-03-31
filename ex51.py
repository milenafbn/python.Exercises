print('+'*20)
print('\033[1;7m10 Termos de uma P.A\033[m')
print('+'*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = int(input('Quantidade de termos: '))
for n in range(1,t + 1):
    print(f'{a1 + (n-1)*r}',end = ' -> ')
print('fim')
    #print(f'{a1} + ({n - 1}) * {r} = {a1 + (n-1)*r}')

