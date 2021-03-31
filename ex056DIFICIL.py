som = 0
Hvelho = 0
Nvelho = ''
a = 0
for c in range(1,5):
    print(f'-----Pessoa {c}-----')
    n = str(input('Nome: '))
    i = int(input('idade: '))
    s = str(input('sexo [M,F]: ')).upper()
    som = som + i
    if i < 20 and s == 'F':
        a = a + 1
    if s == 'M':
       if c == 1:
           Hvelho = i
           Nvelho = n
       else:
           if i > Hvelho:
               Hvelho = i
               Nvelho = n
print(f'A média de todas as idades é {som/4} ')
print(f'Há {a} mulheres com menos de 20 anos ')
print(f'O homem mais velho do grupo é {Nvelho} e tem {Hvelho} anos')


