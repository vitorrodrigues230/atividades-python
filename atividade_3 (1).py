ct_p = 0
ct_i = 0
sp = 0
si = 0
print('Digite [0] para sair')
while True:
       nota = float(input('Digite a nota: '))
       if nota == 0:
           break
       if nota % 2 == 0:
           ct_p += 1
           sp += nota
       else:
           ct_i += 1
           si += nota
mp = sp/ct_p
mi = si/ct_i
print(f'A média aritmética dos números pares é {mp:.1f}')
print(f'A média aritmética dos números ímpares é {mi:.1f}')