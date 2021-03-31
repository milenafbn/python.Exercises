s = 0
cont = 0
while True:
    n = int(input('digte um número (999 stop): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'foram digitados {cont} valores e a soma entre eles foi de {s}')