#o do professor ficou muito diferente
print('+'*30)
print('       BANCO BRADESCO')
print('+'*30)
while True:
    v = float(input('Valor do saque: '))
    a = v % 50
    b = a % 20
    c = b % 10
    if a == 0:
        print(f'Total de {v/50:.1f} cédula de 50')
    else:
        if not v//50 == 0:
            print(f'Total de {v//50} cédula de 50')
    if a != 0:
        if not a//20 == 0:
            print(f'Total de {a//20} cédulas de 20')
    if b != 0:
        if not b//10 == 0:
            print(f'Total de {b//10} cédulas de 10')
    if c != 0:
        if not c == 0:
            print(f'Total de {c} cédulas de 1')
    print('Volte sempre!')
    break



