from datetime import date
hoje = date.today().year
y = int(input('Ano de nascimento: '))
i = hoje - y
print('\033[30mSua categoria é\033[m ')
if i <= 9:
    print('\033[35mMirim\033[m')
elif 9 < i <= 14:
    print('\033[34mInfantil\033[m')
elif 14 < i <= 19:
    print('\033[36mJúnior\033[m')
elif 19 < i <= 25:
    print('\033[33mSênior\033[m')
else:
    print('\033[31mMaster\033[m')
print(f'A idade do atleta é {i} ')
