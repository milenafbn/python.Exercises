n = int(input('Digite um número: '))
print(f'Analisando seu o número {n}')
x = n // 10
y = x // 10
w = y // 10
u = n // 1 % 10
d = x // 1 % 10
c = y // 1 % 10
m = w // 1 % 10
print(f'unidade: {u} ')
print(f'dezena: {d} ')
print(f'centena: {c}')
print(f'milhar: {m} ')

#tipo: 1957/10 o número inteiro que dá é
#195 mas ai sobra 7, que é justamente a unidade
"""n = str(input('Digite um número: ')).zfill(4)
print(f'Analisando seu o número {n}')
print(f'unidade: ', n[3])
print('dezena: ', n[2])
print('centena: ', n[1])
print('milhar: ', n[0])"""
