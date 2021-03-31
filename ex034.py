sal = int(input('Qual seu salário? '))
if sal > 1250:
    print(f'Seu novo salário será \033[7mR${1.10 * sal :.2f}\033[m')
if sal <= 1250:
    print(f'Seu novo salário será \033[7mR${1.15 * sal :.2f}\033[m')
