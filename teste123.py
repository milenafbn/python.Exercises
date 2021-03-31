from time import sleep
from random import randint
c = int(input('\033[30mTabuada = 1\nJogo = 2\n->\033[m '))
if c == 1:
    print('\033[34mVocê escolheu a Tabuada\033[m')
    sleep(2)
    n = int(input('\033[36mDigite um valor:\033[m '))
    print('\033[33m{} x {} = {}'.format(n, 1, n*1))
    print('{} x {} = {}'.format(n, 2, n*2))
    print('{} x {} = {}'.format(n, 3, n*3))
    print('{} x {} = {}'.format(n, 4, n*4))
    print('{} x {} = {}'.format(n, 5, n*5))
    print('{} x {} = {}'.format(n, 6, n*6))
    print('{} x {} = {}'.format(n, 7, n*7))
    print('{} x {} = {}'.format(n, 8, n*8))
    print('{} x {} = {}'.format(n, 9, n*9))
    print('{} x {} = {}'.format(n, 10, n*10))
else:
    print('\033[34mVocê escolheu o Jogo\033[m')
    sleep(2)
    print('\033[35mPensei em um número.')
    sleep(2)
    e = int(input('\033[36mEscolha um número de 0 a 5:\033[m '))
    v = randint(0, 5)
    sleep(2)
    if e == v:
        print('\033[32mParabêns! Você ganhou.\033[m')
    else:
        print('\033[31mVocê perdeu! Eu escolhi {} não {}\033[m'.format(v, e))
