soma = 0
cont = 0
for c in range(1,7):
    a = int(input(f'Digite o {c} valor: '))
    if a % 2 == 0:
        soma += a
        cont += 1
print(f'A soma dos {cont} valores pares resulta em: {soma}')
