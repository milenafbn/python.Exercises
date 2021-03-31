print('@'*30)
print('          SUBMARINO')
print('@'*30)
cont = 0
gasto = 0
maior = 0
menor = 0
mp = ' '
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$ '))
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    gasto += p
    if r == 'N':
        break
    if cont == 1:
        menor = p
        mp = n
    else: #ao invés de ter feito o else, eu poderia ter colocado no if acima um 'or  p < menor:'
        if p < menor:
            menor = p
            mp = n
    if p > 1000:
        maior += 1
print(f'Foram {cont} produtos e o total gasto foi: R${gasto}')
print(f'{maior} produtos passaram de R$1000 ')
print(f'O produto mais barto custou R${menor} e foi o(a) {mp}')