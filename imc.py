print('\033[34;40mIMC\033[m')
p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))
imc = p/(h**2)
print(f'Seu IMC é {imc:.1f}, você está ',end = '')
if imc <= 18.5:
    print('\033[31mabaixo do peso\033[m')
elif imc <= 25:
    print('\033[32mno peso ideal\033[m')
elif imc <= 30:
    print('\033[33mcom sobrepeso\033[m')
elif imc <= 40:
    print('\033[31mcom obesidade\033[m')
else:
    print('\033[30mcom obesidade mórbida\033[m')
