from time import sleep
a = float(input('\033[7;44mPrimeiro valor:\033[m '))
b = float(input('\033[7;44mSegundo valor:\033[m '))
q = 0
while q != 5:
    print('''\033[34m( 1 ) Somar
( 2 ) Multiplicar
( 3 ) maior
( 4 ) novos números 
( 5 ) sair do programa\033[m''')
    q = int(input('\033[7;44mQual é a sua opção?\033[m '))
    if q == 1:
        print(f'A soma entre {a} e {b} é {a + b}')
        print('+++++++++++++++++++++++++++++++')
    if q == 2:
        print(f'A multiplicação entre {a} e {b} é {a * b} ')
        print('+++++++++++++++++++++++++++++++++++++++++')
    if q == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print(f'O maior valor é {maior}')
        print('+++++++++++++++++++')
    if q == 4:
        a = float(input('\033[7;44mPrimeiro valor:\033[m '))
        b = float(input('\033[7;44mSegundo valor:\033[m '))
    if q == 5:
        print('finalizando',end='')
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(1)
        print('.')
        sleep(1.5)
    if q > 5:
        print('Comando inválido. Tente novamente.')
# coisas importantes desse código: maior = a/ maior = b
#Finalizando e os pontinhos aparecendo . . .
# Enquanto q for diferente de 5 você faz isso: ... etc mas dentro do código eu posso colocar um if do 5

