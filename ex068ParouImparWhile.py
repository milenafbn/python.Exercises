from random import randint
print('@' * 30)
print('        Par ou Ímpar')
print('@' * 30)
while True:
    x = int(input('Diga um valor: '))
    a = randint(0, 10)
    b = a + x
    pi = ''
    pi = str(input('Impar ou Par? [p/i] ')).strip().upper()[0] #[0] para pegar só a primeira letra
    print(f'Você jogou {x} e o PC {a}. Total de {b}')
    if pi == 'P':
        if b % 2 == 0:
            print('Você venceu!!\n Vamos jogar novamente...')
        else:
            print('Você perdeu. Jogo finalizado.')
            break
    elif pi == 'I':
        if b % 2 == 1:
            print('Você venceu!!\n Vamos jogar novamente...')
        else:
            print('Você perdeu. Jogo finalizado.')
            break


