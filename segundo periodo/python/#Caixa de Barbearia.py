#Caixa de Barbearia

#Input : Tipo_corte,dia_semana,idade

tipo_corte = input("digite o tipo de corte[Cabelo],[Barba] ou[Combo]: ")
dia_semana = input("digite o dia da semana por extenso: ")
idade = int(input("digite sua idade: "))

#cabelo = 30 reais, barba = 40 reais,combo = 60 reais
#definição de valores por tipo
if tipo_corte == "cabelo":
    valor_inicial = 30
elif tipo_corte == "barba":
    valor_inicial = 40
elif tipo_corte == "combo":
    valor_inicial = 60

#calculo de acressimo e desconto em Reais
desconto = 0
acressimo = 0
if tipo_corte == "cabelo" or tipo_corte == "combo":
    if idade < 12 or idade > 60:
        desconto += 10
if dia_semana == "terça" or dia_semana == "quarta":
    desconto += 5
elif dia_semana == "quinta":
    if tipo_corte == "combo":
        desconto += 10 
elif dia_semana == "sabado":
    acressimo = 10

#calculo valor final 
valor_final = valor_inicial + acressimo - desconto
print(f"valor final = {valor_final}, desconto aplicado = {desconto},acressimo aplicado = {acressimo}")