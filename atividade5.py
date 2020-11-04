#funcao = lambda y: return yh = funcao(4)print(h)
#A resposta é sintaxe inválida.
#Não precisava fazer isso aqui mas achei que ia ficar legal kkkkk
def pergunta():
    print('''
Dado o trecho de código funcao = lambda y: return yh = funcao(4)print(h), 
assinale a alternativa que corresponde ao resultado da execução dele.
1-4
2-0
3-erro de sintaxe
4-retorno 4 
    ''')
    opcoes()
def opcoes():
    op=int(input("Insira a opção escolhida: "))
    if op==1:
        print("Incorreto!")
        return pergunta()
    elif op==2:
        print("Incorreto!")
        return pergunta()
    elif op==3:
        print("Correto!")
        SystemExit
    elif op==4:
        print("Incorreto!")
        return pergunta()
pergunta()