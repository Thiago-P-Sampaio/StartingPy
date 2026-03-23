#Exercício 2.2
#  Valor final ->  custo de fábrica + custo de imposto(25%) + custo de revendedor(45%)
taxes = (25/100) # Impostos
car_dealer = (45/100) # Revendedor

print("Algoritmo que realiza o cálculo do valor final de um veículo ")

car_price = float(input("Valor do véiculo(Fábrica) R$: "))
taxes *= car_price
car_dealer *= car_price
final_price = car_price + taxes + car_dealer

print("Fábrica: ", car_price)
print(" Imposto: ", taxes)
print(" Revendedor: ", car_dealer)
print(" Preço final R$: ", final_price)