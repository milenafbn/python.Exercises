a = float(input('Nota do primeiro bimestre: '))
b = float(input('Nota do segundo bimestre: '))
m = (a + b)/2
if m <= 5:
    print('\033[31mREPROVADO\033[m')
elif 5 < m <= 6.9:
    print('\033[33mRECUPERAÇÂO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
print(f'Sua média foi {m}')