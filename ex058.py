from random import choice
b = 1
x = choice([1,2,3,4,5,6,7,8,9])
print('\033[7mPensei em um número entre 0 e 10\033[m\n\033[7mConsegue adivinhar? tente abaixo:\033[m ')
a = int(input('👉 '))
while a != x:
    if a > x:
        print(f'\033[36mMenos que {a}\033[m')
    if a < x:
        print(f'\033[36mMais que {a}\033[m')
    a = int(input('Tente novamente: '))
    b = b + 1
print(f'\033[32mDepois de {b} tentativas você Acertou! o número escolhido pelo computador foi {x}\033[m ')