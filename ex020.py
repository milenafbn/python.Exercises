from random import shuffle
print('Ordem de apresentação')
a = str(input('aluno 1: '))
b = str(input('aluno 2: '))
c = str(input('aluno 3: '))
d = str(input('aluno 4: '))
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')







