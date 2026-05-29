estoque = {"caneta": 3, "borracha": 0, "caderno": 5, "lapis": 0, "régua": 2}

disponivel = {v: k for k, v in estoque.items() if v > 0}

print(disponivel)
