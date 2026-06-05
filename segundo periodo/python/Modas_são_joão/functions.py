'''Aqui serão armazenadas as funções CRUD que serão usadas no arquivo principal main.py'''

def criar_novo_registro():
    from dados import dicionario_produto,tamanhos_fixos #importa os dados para tratamento de erros

    nome = input("digite o nome do cliente: ")
    idade = input("digite a idade do cliente: ")
    produto = input("digite a roupa que o cliente escolheu: ")
    tamanho_roupa = input("digite o tamanho da roupa de escolha do cliente: ")

    try: #idade com numero incorreto
        idade = int(idade)

    except ValueError:
        print("ops você digitou número invválido, por favor tente novamente!!!")
        return 0

    if produto not in dicionario_produto: #produto invalido
        print("ops você digitou um produto inválido, por favor tente novamente!!")
        return 0

    if tamanho_roupa not in tamanhos_fixos: #tamanho invalido
        print("ops você digitou um tamanho inválido, por favor tente novamente!!!")
        return 0
    
    if idade > 12 and idade < 18: #define o tipo de linha de roupa sendo juvenil ou adulta 
        linha_produto = "juvenil"

    elif idade < 60: 
        linha_produto = "adulto"
    else: 
        print("a idade digitada não é contemplada pelos produto da loja tente novamente!!!") #caso a idade não seja adulta e nem infantil
        return 0

