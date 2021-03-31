x = 0
sn = 0
cont = som = 0
menor = 0
maior = 0
while not sn == 'N':
    x = int(input('Digite um número: '))
    sn = str(input('Deseja continuar? (S/N) ')).upper()
    cont += 1
    som += x
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
print(f'''Você digitou {cont} números, a média deles foi {som/cont}
O maior valor é {maior} e o menor {menor}''')
