#Faça um programa que solicite o nome do usuário e a idade do usuário,
#depois disso exiba a mensagem: “{nome} possui {idade} anos.”.

nomeIdade=lambda nome,idade:print("O usuário de nome",{nome},"possui a idade de",{idade},"anos.")
nomeUsuario=str(input("Insira seu nome: "))
idadeUsuario=int(input("Insira sua idade: "))
nomeIdade(nomeUsuario,idadeUsuario)
