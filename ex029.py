v = float(input('Qual era a velocidade do carro? '))
if v > 80:
    print(f'\033[31mVocê excedeu o limite permitido que é de 80Km/h. Pagará uma multa de R${(v-80)*7 :.2f}\033[m')
else:
    print('\033[36mparabéns! Continue respeitando o limite permitido que é de 80Km/h\033[m')