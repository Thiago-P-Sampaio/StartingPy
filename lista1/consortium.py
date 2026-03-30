# Exerc 2.8
# número total de prestações
# quantidade de prestações pagas
# valor da prestação
# RESULTADO --> TOTAL PAGO E SALDO DEVENDOO

#1. Valor prestação * quantidade de prestações = valor de consórcio
#2. Valor da prestação * quantidade de prestações pagas = valor pago até o momento
#3. Valor do consórcio - valor pago até o momento = saldo devedor


print("Algoritmo que calcula valor de consórcio")

total_prestacoes = int(input("Informe o número total de prestações: "))
prestacoes_pagas = int(input("Informe o total de prestações pagas até o momento: "))

if prestacoes_pagas <= total_prestacoes:
    valor_prestacao = float(input("Informe o valor das prestações: "))
    valor_pago = prestacoes_pagas * valor_prestacao
    saldo_devedor = (total_prestacoes * valor_prestacao) - valor_pago
    print(f"O consorciado pagou R${valor_pago}, e portanto deve do total de R${total_prestacoes * valor_prestacao}, a quantidade de R${saldo_devedor}")
else:
    print("Inconsistência detectada, as prestações pagas não podem ser superiores ao total")
