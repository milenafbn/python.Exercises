v = float(input('Qual foi a distância da viagem? '))
if v <= 200:
    print(f'\033[7;30;43mO custo da viagem será de R${v * 0.5 :.2f}\033[m')
else:
    print(f'\033[7;30;43mO custo da viagem será de R${v * 0.45 :.2f}\033[m')


