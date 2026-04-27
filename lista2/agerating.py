#Exerc 9
print("============= Algoritmo de classifica idades de atletas ============= ")

nome = str(input("Nome do atleta: "))
altura = int(input("Altura do atleta em cm: "))
idade = int(input("idade do atleta: "))
peso = int(input("peso do atleta em KG: "))

if idade >= 5 and idade <= 10:
    print(f"O(A) atleta {nome} com altura de {altura/100:.2f} metros e peso igual a {peso}KG participa da categoria infantil")
if idade >= 11 and idade <= 17:
    print(f"O(A) atleta {nome} com altura de {altura/100:.2f} metros e peso igual a {peso}KG participa da categoria juvenil")
if idade >= 18:
    print(f"O(A) atleta {nome} com altura de {altura/100:.2f} metros e peso igual a {peso}KG participa da categoria sênior")
