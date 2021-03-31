print('+'*11)
print(' Tabuada ')
print('+'*11)
while True:
    n = int(input('Qual tabuada você quer ver? '))
    if n <= 0: #se colocar embaixo ele não vai parar
        break
    print('+'*30)
    for c in range (1,11):
        print(f'{n} x {c} = {c * n}')
    print('+'*30)
