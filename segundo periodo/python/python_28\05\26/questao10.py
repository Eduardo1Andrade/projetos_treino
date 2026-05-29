def parsear_temps(entradas):
    for item in entradas:
        try:
            yield float(item)
        except:
            yield None

entradas = ["0", "100", "erro", "37", "abc", "-40", "25"]

fahrenheit = [round(c * 9/5 + 32, 1) for c in parsear_temps(entradas) if c is not None]

print(fahrenheit)
