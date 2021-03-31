a = float(input('\033[7mDigite um número:\033[m '))
b = float(input('\033[7mDigite outro número:\033[m '))
if a>b:
    print('\033[40mO primeiro número é maior\033[m')
elif b>a:
    print('\033[40mO segundo número é maior\033[m')
else:
    print('\033[40mNão há maior, são iguais\033[m')