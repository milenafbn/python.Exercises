soma = 0
cont = 0
for x in range(3 , 501 ,6): # poderia ter colocado um if c % 3 == 0: ai tab e os bichinhos ai de baixo
    soma = soma + x #ou soma += c
    cont = cont + 1 #cont += 1
print(f'A soma dos {cont} termos é {soma}')

