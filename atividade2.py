#Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 

doisNumeros=lambda valorUm,valorDois:valorUm*valorDois
valorP=int(input("Insira um valor inteiro: "))
valorS=int(input("Insira outro valor inteiro: "))
valorFinal=doisNumeros(valorP,valorS)
print("O resultado final da multiplicação",valorP,"x",valorS,"é:",valorFinal)

