casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
ano = float(input('Em quantos anos deseja pagar? '))
p = 12 * ano
pm = casa / p
e = pm / sal
if (100 * pm)/sal >= 30:
    print(f'\033[31mSeu empréstimo foi negado pois excede ou se iguala a 30% do seu salário, sendo a prestação {pm}\033[m')
else:
    print(f'\033[32mSeu empréstimo foi aprovado, a prestação será {pm}, não excedendo o limite de 30% do seu salário\033[m')