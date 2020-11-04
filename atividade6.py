#Faça um programa utilizando expressões lambda para gerar o quadrado, o triplo de um número.

numeroQuadrado=lambda valorInicial:valorInicial**2
numeroTriplo=lambda valorInicial:valorInicial**3

valorInicial=int(input("Insira um número: "))
valorQuadrado=numeroQuadrado(valorInicial)
valorTriplo=numeroTriplo(valorInicial)
print(f'''
VALORES:
O quadrado de {valorInicial} é = {valorQuadrado} 
O triplo de {valorInicial} é = {valorTriplo}
''' )