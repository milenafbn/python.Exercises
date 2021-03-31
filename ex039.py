from datetime import date
atual = date.today().year
nas = int(input('Qual seu ano de nascimento? '))
a = atual - nas
falta = 18 - a
pas = a - 18
ali = 18 + nas
if a == 18:
    print('Está na hora de se alistar, soldado!')
elif a > 18:
    print(f'Já passou do prazo faz {pas} anos\n Seu alistamento foi em {ali}')
else:
    if falta == 1:
        print(f'Está quase! falta 1 ano ')
    else:
        print(f'Ainda faltam {falta} anos\n Será em {ali}')
