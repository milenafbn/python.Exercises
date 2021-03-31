x = int(input('Digite um número (0 para parar): '))
b = x #criei outra variável pq o código não tava contando com esse primeiro x já que o x em baixo passou a ser
# só o dentro do while
cont = 0
som = 0
while not x == 0:
    x = int(input('Digite um número (0 para parar): '))
    cont += 1
    som += x
print(f'Você digitou {cont} números e a soma deles foi {som + b} ')