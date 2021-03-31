s = str(input('Qual seu sexo? ')).upper().strip()[0]
while s != 'F' and s != 'M':
    s = str(input('\033[31mDados inválidos. Digite F ou M: \033[m')).upper().strip()[0]
print('\033[32mDado cadastrado!\033[m')
#com o [0] eu posso digitar masculino/feminino e ele vai pegar só a inicial