#Faça um programa que solicite dez números ao usuário, depois disso,
#exiba todos números pares e só então exiba todos os números ímpares.
#Utilize a função filter para fazer isso.

numeros=[]
for x in range(0,10):
    numero=int(input("Insira um número par, ou ímpar: "))
    numeros.append(numero)
pares = [x for x in numeros if x%2==0]
impares = [x for x in numeros if x%2!=0]
print(f'''Os números pares são: {pares}
Os números ímpares são:{impares}''')
