print('Gerador P.A')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = 0
while not x == 10: #enquanto x (que é meu n da P.A) não for igual a 10 (pq quero 10 termos), ele vai rodar até chegar no nono (10-1) elemento
    x += 1
    print(f' {a1 + (x-1)*r} ',end='')
    if x == 10: #if pq se colocar a seta no print acima no último número ela aparece na frente e não tem nada,
        print('',end='') #fica feio, então coloquei essa condição
    else:
        print('➭',end='')