'''Aqui serão armazenadas as funções CRUD que serão usadas no arquivo principal main.py'''

def criar_novo_registro():
    '''cria registro de venda de acordo com nome da pessoa,roupa escolhida,tamanho escolhido ,idade da pessoa 
    e armazena em um dict
    
    Arg: none

    Returns: Dict de registros atualizado

    '''
    from dados import dicionario_produto,tamanhos_fixos, id_atual,dicionario_registros #importa os dados para tratamento de erros

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

    if linha_produto == "juvenil": #aplica preco com base na linha jovem ou adulta
        preco = dicionario_produto[produto]["preco_base_juvenil"]

    elif linha_produto == "adulto":
        preco = dicionario_produto[produto]["preco_base_adulto"]

    else:
        print("ops erro ao definir preço")

    if tamanho_roupa == "M": #se for p o preco é o mesmo do preco base, se for maior aumenta em 20% em tamanho M e 40# em tamanho G
        preco = preco * 1.2
    elif tamanho_roupa == "G":
        preco = preco * 1.4 
    
    nome = nome.strip()
    nome = nome.casefold()
    nome = nome.title() #metodos para Formatação de string

    dicionario_registros[f"registro_id_{id_atual + 1}"] = { #criação do dict de registro
        "nome" : nome,
        "idade" : idade,
        "id" : id_atual + 1,
        "tamanho" : tamanho_roupa,
        "linha" : linha_produto,
        "preco" : preco
    }
    print(dicionario_registros)
    return 0



    
    

