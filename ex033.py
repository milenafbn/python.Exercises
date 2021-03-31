a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
if a>b>c or a>c>b:
    print(f'\033[7;46m{a} é o maior valor\033[m ')
if b>a and c>a:
    print(f'\033[7;45m{a} é o menor valor\033[m')
if b>a>c or b>c>a:
    print(f'\033[7;46m{b} é o maior valor\033[m')
if a>b and c>b:
    print(f'\033[7;45m{b} é o menor valor\033[m')
if c>a>b or c>b>a:
    print(f'\033[7;46m{c} é o maior valor\033[m')
if a>c and b>c:
    print(f'\033[7;45m{c} é o menor valor\033[m')
