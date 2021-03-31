print('{:+^40}'.format('LOJAS AMERICANAS'))
v = float(input('Preço das compras: R$  '))
print('\033[1;4;40mFormas de pagamento\033[m')
print('''\033[1;30m( 1 ) À vista dinheiro/cheque
( 2 ) À vista cartão
( 3 ) 2x no cartão
( 4 ) 3x ou mais no cartão\033[m ''')
o = int(input('Qual a opção? '))
if o == 1:
    print(f'Você pagará R${0.9 * v :.2f}')
elif o == 2:
    print(f'Você pagará R${0.95 * v :.2f}')
elif o == 3:
    print(f'Você pagará o mesmo valor de R${v} em 2x por parcelas de R${v/2:.2f}')
elif o == 4:
    p = int(input('Quantas parcelas? '))
    print(f'Você pagará R${1.2 * v :.2f} em parcelas de {p}x por R${(1.2 * v)/p :.2f} (com juros)')
else:
    print('\033[31mOpção não identificada, tente novamente\033[m')

