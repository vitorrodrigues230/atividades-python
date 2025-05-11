r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 == r3:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('É um triângulo equilátero')
    else:
        print('Não é um triângulo')
elif r1 != r2 != r3:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('É um triângulo escaleno')
    else:
        print('Não é um triângulo')
elif r1 != r2 == r3 or r2 != r1 == r3 or r3 != r2 == r1:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('É um triângulo isosceles')
    else:
        print('Não é um triângulo')