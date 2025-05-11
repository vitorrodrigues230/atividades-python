ct=0
soma=0
sorvete=0
print('Digite o número[-1] para sair')
while True:
    numero=float(input('Digite o valor: '))
    if numero==-1:
        break
    ct=ct+1
    soma=soma+numero
    if numero>20:
        sorvete=sorvete+1
media= soma/ct
print('Quantidade de números:',ct)
print(f'A média dos valores digitados: {media:.2f}')
print('A soma dos valores são:',soma)
print('A quantidade de números 20 são:',sorvete)