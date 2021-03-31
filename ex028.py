from random import choice
from time import sleep
x = int(input('Digite um número de 0 a 5: '))
n = choice([0,1,2,3,4,5])
print('\033[34mProcessando...\033[m')
sleep(2)
if x == n:
    print('\033[32mParabéns,você acertou!\033[m')
else:
    print('\033[31merrou otário, tenta de novo\033[m')
    print(f'O número certo era {n}')




