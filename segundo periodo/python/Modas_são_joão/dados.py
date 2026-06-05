''' aqui ficaram os tipos de dados guardados que serão usados na função main.py'''
lista_registro = [] # guarda os dicts de registros

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
categorias_roupas = ("adulta","juvenil") # lista imutavel de categoria de roupas

tamanhos_fixos = ("P","M","G") # lista imutavel de tamanhos
dicionario_produto = { #armazena os preços dos produtos disponiveis, #cada tamanho aumenta o preço em 20% transformando em int
    "chapeu" : {
        "preco_base_juvenil" : 25,
        "preco_base_adulto" : 40
    },
    "vestido" : {
        "preco_base_juvenil" : 30,
        "preco_base_adulto" : 45
    },
    "Calça" : {
        "preco_base_juvenil" : 25,
        "preco_base_adulto" : 40
    },
    "Camisa" : {
        "preco_base_juvenil" : 25,
        "preco_base_adulto" : 40
    },
} 