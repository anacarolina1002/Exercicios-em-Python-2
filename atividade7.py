#Faça um programa que leia duas notas de um aluno numa turma de 10 alunos.
#Para cada aluno, calcular a média ponderadas das notas, sabendo que a nota1 tem peso = 4
#e a nota2 tem peso = 6 . Imprimir a média do aluno e o conceito final,
#conforme tabela abaixo:    
#Intervalo      Conceito
# 0,0 a 4,9        D
# 5,0 a 6,9        C
# 7,0 a 8,9        B
# 9,0 a 10,0       A
#Fazer 2 funções:Função lambda para calcular a média ponderada das notas.
#Argumentos de entrada duas notas, Saída a média.
#Função local que irá receber como argumento de entrada a média das notas
#e retornar o conceito conforme a tabela acima.
medPonderada=lambda nota1,nota2: nota1*0.4+nota2*0.6#calculo da média, multiplica a nota pelos valores e retorna um número entre 0 e 10 no final

def conceito(mediaAluno):#validações das médias
    if mediaAluno<=5.0 and mediaAluno>=0:
        letraConceito="D"
    elif mediaAluno<=7.0 and mediaAluno>5.0:
        letraConceito="C"
    elif mediaAluno<9.0 and mediaAluno>7.0:
        letraConceito="B"
    elif mediaAluno>=9 and mediaAluno<=10:
        letraConceito="A"
    return letraConceito#retorna o conceito que está dentro de alguma validação

for x in range (0,10):
    notaP=float(input("Insira sua primeira nota:"))#pedido das notas
    notaS=float(input("Insira sua segunda nota:"))
    print("Preparando nota",notaP,"e nota",notaS,"para cálculo de média...")#enfeite kkk
    mediaAluno=medPonderada(notaP,notaS)#a medPonderada é atribuida a uma variável pra poder ser colocada no print
    conceitoX=conceito(mediaAluno)#conceito a mesma coisa, atruibui a variavel
    print(f'''
O aluno possui média igual a {mediaAluno}
O aluno possui o conceito igual a {conceitoX} 
    ''')#print final




