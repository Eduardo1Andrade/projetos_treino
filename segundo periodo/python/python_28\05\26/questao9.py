def calcular_imc(peso, altura):
    if not isinstance(peso, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Peso e altura devem ser números")

    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")

    return round(peso / (altura ** 2), 2)

casos = [
    (70, 1.75),
    ("70", 1.75),
    (70, 0)
]

for peso, altura in casos:
    try:
        print(calcular_imc(peso, altura))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
