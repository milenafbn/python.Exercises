maior = 0
menor = 0
cont = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}* pessoa: '))
    cont += 1
    if cont == 1:
        maior = menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} ')
print(f'O menor peso é {menor} ')
#deu erro no menor peso e nao sei pq, tá igual ao do professor