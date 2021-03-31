from random import choice
from time import sleep
print('\033[7;36mPEDRA, PAPEL e TESOURA!\033[m')
print('''\033[1;36m( 1 ) Pedra
( 2 ) Papel 
( 3 ) Tesoura\033[m''')
pc = choice(['pedra', 'papel', 'tesoura'])
h = int(input('Qual sua jogada? '))
print('\033[7m3...\033[m')
sleep(1)
print('\033[7m2...\033[m')
sleep(1)
print('\033[7m1...\033[m')
sleep(1)
print(f'O computador jogou {pc}')
if h == 1:
    if pc == 'tesoura':
        print('\033[32mVocê ganhou!\033[m')
    elif pc == 'papel':
        print('\033[31mVocê perdeu!\033[m')
    else:
        print('\033[33mEmpate!\033[m')
elif h == 2:
    if pc == 'tesoura':
        print('\033[31mVocê perdeu!\033[m')
    elif pc == 'pedra':
        print('\033[32mVocê ganhou!\033[m')
    else:
        print('\033[33mEmpate!\033[m')
elif h == 3:
    if pc == 'papel':
        print('\033[32mVocê ganhou!\033[m')
    elif pc == 'pedra':
        print('\033[31mVocê perdeu!\033[m')
    else:
        print('\033[33mEmpate!\033[m')
else:
    print('\033[31mOpção inválida. Tente novamente\033[m')

