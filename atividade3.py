#Faça um programa que solicite cinco números ao usuário, depois disso,
# exiba apenas os números maiores do que 10. Utilize a função filter para fazer isso.

numeros = []
for x in range(0,5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
filtrados = [x for x in numeros if x >= 10]
print("Os números maiores que 10 são:",filtrados)