f = str(input('Digite uma frase/nome: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = j[::-1]
if j == i:
    print(f'\033[32mSua texto é um palíndromo!\033[m invertido fica {i.title()}')
else:
    print(f'\033[31mseu texto NÃO é um palíndromo!\033[m invertido fica {i}')