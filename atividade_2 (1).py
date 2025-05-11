ct=0
cf=0
cg=0
print('Digite[-1] para parar')
while True:
    nota=float(input("Digite a nota do aluno: "))
    if nota==-1:
        break
    ct=ct+1
    if nota>=5:
        cf=cf+1
    if nota<5:
        cg=cg+1
print('O número de alunos que fez a prova:',ct)
print('Quantidade de alunos aprovados:',cf)
print("Quantidade de alunos reprovados:",cg)

