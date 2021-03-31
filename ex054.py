from datetime import date
som = 0
b = 0
for i in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    a = date.today().year
    if a - ano < 18:
        som = som + 1
    else:
        b = b + 1
print(f'São {som} menores de idade')
print(f'São {b} maiores de idade')
