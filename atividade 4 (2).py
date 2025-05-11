ct=0
soma=0
y=int(input("qual o valor final:"))
for num in range (0,y,1):
    print(num)
    ct=ct+1
    soma=soma+num
media=soma/ct
print("quantidade de numeros",ct)
print("soma dos numeros",soma)
print("media",media)
