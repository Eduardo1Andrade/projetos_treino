
def listar_produtos():
    '''lista produtos'''
    import dados
    lista_produtos = [dados.dicionario_produto for produto in dados.dicionario_produto.keys()]
    print(lista_produtos)

def gerar_tamanho(indice):
    import dados
    '''gera tamanhos dos produtos'''

    contador = 0
    while contador < indice:
        yield dados.tamanhos_fixos[contador]
        contador += 1
    