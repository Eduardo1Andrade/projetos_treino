''' aqui ficaram os tipos de dados guardados que serão usados na função main.py'''
dicionario_registros = {}

# exemplo de estrutura dict 

#registro_id(0,1,2....) = {
#    nome : str "nome"
#    idade : int "idade"
#    produto : {
#       nome_produto :  str "nome"      
#       tamanho_produto :  str "tamanho"
 #      preco : float "preco"
#        }
#}
categorias_roupas = ("adulto","juvenil") # lista imutavel de categoria de roupas

tamanhos_fixos = ("P","M","G") # lista imutavel de tamanhos

id_atual = 0 # registro de id dos produtos , começando em 0

dicionario_produto = { #armazena os preços dos produtos disponiveis, #cada tamanho aumenta o preço em 20% transformando em int
    "chapeu" : {
        "preco_base_juvenil" : 25.0,
        "preco_base_adulto" : 40.0
    },
    "vestido" : {
        "preco_base_juvenil" : 30.0,
        "preco_base_adulto" : 45.0
    },
    "calça" : {
        "preco_base_juvenil" : 25.0,
        "preco_base_adulto" : 40.0
    },
    "camisa" : {
        "preco_base_juvenil" : 25.0,
        "preco_base_adulto" : 40.0
    },
} 