print('-'*30)
print('Cadastro de pessoas')
print('-'*30)
cont = 0
h = 0
m = 0
while True:
    print('+'*20)
    i = int(input('idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('sexo [M/F]: ')).strip().upper()
    print('+'*20)
    if i > 18:
        cont = cont + 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m += 1
    p = ' '
    while p not in 'SN': #se a pessoa digitar outra coisa sem ser s ou n ele vai perguntar de novo
        p = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if p == 'N':
        break
print(f'Há {cont} pessoas com mais de 18 anos ')
print(f'Há {h} homens cadastrados')
print(f'Há {m} mulheres com menos de 20 anos')