'''Aqui serão armazenadas as funções CRUD que serão usadas no arquivo principal main.py'''

def criar_novo_registro():
    '''cria registro de venda de acordo com nome da pessoa,roupa escolhida,tamanho escolhido ,idade da pessoa 
    e armazena em um dict
    '''
    import dados  #importa os dados para tratamento de erros

    nome = input("digite o nome do cliente: ")
    idade = input("digite a idade do cliente: ")
    produto = input("digite a roupa que o cliente escolheu [camisa,calça,chapeu,vestido]:  ")
    tamanho_roupa = input("digite o tamanho da roupa de escolha do cliente [P,M,G]: ")

    try: #idade com numero incorreto
        idade = int(idade)

    except ValueError:
        print("ops você digitou número invválido, por favor tente novamente!!!")
        return 0

    if produto not in dados.dicionario_produto: #produto invalido
        print("ops você digitou um produto inválido, por favor tente novamente!!")
        return 0

    if tamanho_roupa not in dados.tamanhos_fixos: #tamanho invalido
        print("ops você digitou um tamanho inválido, por favor tente novamente!!!")
        return 0
    
    if idade > 12 and idade < 18: #define o tipo de categoria de roupa sendo juvenil ou adulta 
        categoria_produto = "juvenil"

    elif idade < 60: 
        categoria_produto = "adulto"
    else: 
        print("a idade digitada não é contemplada pelos produto da loja tente novamente!!!") #caso a idade não seja adulta e nem infantil
        return 0

    if categoria_produto == "juvenil": #aplica preco com base na categoria jovem ou adulta
        preco = dados.dicionario_produto[produto]["preco_base_juvenil"]

    elif categoria_produto == "adulto":
        preco = dados.dicionario_produto[produto]["preco_base_adulto"]

    else:
        print("ops erro ao definir preço")

    if tamanho_roupa == "M": #se for p o preco é o mesmo do preco base, se for maior aumenta em 20% em tamanho M e 40# em tamanho G
        preco = preco * 1.2
    elif tamanho_roupa == "G":
        preco = preco * 1.4 
    
    nome = nome.strip()
    nome = nome.casefold()
    nome = nome.title() #metodos para Formatação de string


    dados.dicionario_registros[dados.id_atual] = { #criação do dict de registro
        "nome" : nome,
        "idade" : idade,
        "id" : dados.id_atual,
        "produto" : produto,
        "tamanho" : tamanho_roupa,
        "categoria" : categoria_produto,
        "preco" : preco
    }

    dados.id_atual += 1
    print("registro criado com sucesso!!!")

    return dados.dicionario_registros

def editar_registro():
    ''' função que permite editar um registros seja nome ou idade do cliente,produto,tamanho,categoria ou preço mas não permite editar o id'''
    import dados 


    id_editar = input("digite o ID do registro para editar: ") #para fazer a busca por id

    try: #id com numero incorreto
        id_editar = int(id_editar)

    except ValueError: 
        print("ops você digitou número invválido, por favor tente novamente!!!")
        return 0

    try:
        registro_id = dados.dicionario_registros[id_editar]

    except KeyError: #caso o id não exista
        print("ops registro não encontrado ou inexistente!!!")
        return 0

    while True: #para poder continuar editando até que escolha sair
        comando = input('''selecione um comando:
            Editar nome[1]
            Editar idade[2]
            Editar produto[3]
            Editar tamanho[4]
            Editar categoria[5]
            Editar preço[6]
            Sair[7]
        :''')
        if comando == "1": #permite editar nome
            print("você escolheu editar nome!!")

            novo_nome = input("digite o novo nome: ")

            novo_nome = novo_nome.strip()
            novo_nome = novo_nome.casefold()
            novo_nome = novo_nome.title()

            print("processando edição...")
            
            registro_id["nome"] = novo_nome

            print("novo nome registrado com sucesso!!")
            return registro_id

        elif comando == "2": #permite editar a idade do usuario idependente se passar das regras de ter menos de 14 ou mais 60 anos
            print("você escolheu editar idade!!")

            novo_idade = input("digite o novo idade: ")   

            try: #id com numero incorreto
                novo_idade = int(novo_idade)

            except ValueError:
                print("ops você digitou número invválido, por favor tente novamente!!!")
                return 0

            print("processando edição...")

            registro_id["idade"] = novo_idade

            print("nova idade registrado com sucesso!!")
            pass

        elif comando == "3": #permite editar o nome do produto se for valido
            print("você escolheu editar produto!!")

            novo_produto = input("digite o nome do produto: ")
            if novo_produto not in dados.dicionario_produto:
                print("produto invalido por favor tente novamente!!")
                pass
            
            print("processando edição....")
            
            registro_id["produto"] = novo_produto

            print("novo produto editado com sucesso!!")
            pass

        
        elif comando == "4": #permite editar tamanho da roupa
            print("você escolheu editar tamanho!!")

            novo_tamanho = input("digite o nome do tamanho: ")
            if novo_tamanho not in dados.tamanhos_fixos:
                print("tamanho invalido por favor tente novamente!!")
                pass
            
            print("processando edição....")
            
            registro_id["tamanho"] = novo_tamanho

            print("novo tamanho editado com sucesso!!")
            pass
            
        elif comando == "5": #permite editar categoria de roupa
            print("você escolheu editar categoria de roupa!!")

            novo_categoria = input("digite o nome da categoria de roupa: ")
            if novo_categoria not in dados.categorias_roupas:
                print("categoria de roupa invalido por favor tente novamente!!")
                pass
            
            print("processando edição....")
            
            registro_id["categoria"] = novo_categoria

            print("novo categoria editado com sucesso!!")
            pass

        elif comando == "6": #permite editar
            print("você escolheu editar preço!!")

            novo_preco = input("digite o nome do preco: ")

            try: #para erro de valor incorreto
                novo_preco = float(novo_preco)
            except ValueError:
                print("ops numero invalido por favor tente novamente!!!")
                pass            

            print("processando edição....")
            
            registro_id["preco"] = novo_preco

            print("novo preco editado com sucesso!!")
            pass

        elif comando == "7": #permite sair
            break
        else:
            print("você digitou um comando invalido por favor tente novamente!!")
            pass
    
def excluir_registro(): #para exluir um registro por id
    '''função que permite exluir um registro por ID com confirmação do uúsario '''
    import dados
    id_excluir = input("digite o ID do registro a ser excluido: ")
    
    try:
        id_excluir = int(id_excluir)
    except ValueError: #verifica se o id é numero
        print("ops numero invalido tente novamente!!!")
        return 0
    
    confirmacao = input(f"você realmente deseja excluir o item de Id = {id_excluir} ?[sim] ou [nao]: ")

    if confirmacao == "sim":
        print("excluindo....")

        try: #trata caso o item não exista
            dados.dicionario_registros.pop(id_excluir)
        except KeyError:
            print("ops registro invalido ou inexistente!!!!")
            return 0
        print("item excluido com sucesso!!!")
    
    elif confirmacao == "nao":
        print("exclusão cancelada!!")
        return 0
    
    else:
        print("comando invalido!!")
        return 0

    
def listar_registro():

    '''função que lista todos os registros com formação '''
    import dados

    try: #trata caso exista algo para listar
        for id_registro, registro in dados.dicionario_registros.items():
            print(f"Registro {id_registro}")
    
            for chave, valor in registro.items():
                print(f"{chave} : {valor}")
    
            print("-" * 20)

        return 0

    except UnboundLocalError:
        print("nao há registros !!!!")

def buscar_registro():
    '''função que permite a busca de um registro em expecifico por ID'''
    import dados
    id_busca = input("digite o id do registro a ser buscado: ")

    try: #tenta tratar se é numero
        id_busca = int(id_busca)

    except ValueError:
        print("digite um numero valido!!")
        return 0

    if id_busca not in dados.dicionario_registros:#caso o item não exista na lista
        print("ops registro não encontrado ou inexistente!!!")
        return 0
    
    for chave, valor in dados.dicionario_registros[id_busca].items():
        print(f"{chave} : {valor}")

    print("-" * 20)
    return 0

def gerar_relatorio():
    '''função que gera um relatorio simples de numero de vendas e saldo final'''
    import dados

    saldo = 0 
    vendas = 0

    try:
        for id_valor in dados.dicionario_registros.values():
            venda += 1
            saldo += id_valor["preco"]
    except UnboundLocalError:
        print("não há registros!!!")
    
    print(f"Saldo Final: {saldo:.2f}, Número de Vendas = {venda}")
    return 0

#tava acontecendo um bug de unbound erro e para evitar coloquei um try para tratar disso que é para quando não term algo a ser listado no for na função listar_registro