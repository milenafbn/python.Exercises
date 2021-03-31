print( '\033[7mConversor binário, octal e hexadecimal\033[m')
num = int(input('Digite o número: '))
print(' \033[34;40m [ 1 ] Para Binário\033[m\n \033[36;40m [ 2 ] Para octal\033[m\n \033[35;40m [ 3 ] Para hexadecimal\033[m')
x = int(input('Qual será a base numérica? '))
if x == 1:
    print(f'Para binário fica {bin(num) [2:]}')
elif x == 2:
    print(f'Para Octal fica {oct(num) [2:]}')
elif x == 3:
    print(f'Para hexadecimal fica {hex(num) [2:]}')
else:
    print('Opção inválida, tente novamente')

