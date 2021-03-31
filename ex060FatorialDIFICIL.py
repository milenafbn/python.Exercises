n = int(input('Digite um número: '))
print('Seu fatorial é ',end='')
print(f'{n}! = {n}',end='')
c = n
f = 1
while c > 1 :
    f *= c #nesse caso o c vai subtraindo 1 pra fazer o fatorial
    c -= 1
    print(f' x {c}',end='') # fica repetindo o c - 1 até ele não ser maior que 1 
print(f' = {f}',end='')

#outra forma de fazer com for:
'''print(f'{n}! = ',end='')
for c in range(n+1,1,-1):
    c -= 1
    f *= c
    print(f'{c}', end='')
    if c == 1:
        print(' = ',end='')
    else:
        print(' x ',end='')
print(f'{f}')'''