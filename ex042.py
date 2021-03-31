a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('É um triângulo equilátero!')
    if a == b and a != c:
        print('É um triângulo isóceles!')
    if a == c and a != b:
        print('É um triângulo isóceles!')
    if b == c and b != a:
        print('É um triângulo isóceles!')
    if a != b and a != c and b != c:
        print('É um triângulo escaleno!')
else:
    print('Os segmentos não formam um triângulo')
# pra ficar mais fácil era melhor que tu fizesse a!= b != c MAS da erro pq o a pode ser
# igual ao c... então tu faz a!= b != c != a