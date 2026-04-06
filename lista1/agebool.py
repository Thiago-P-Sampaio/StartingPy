## Exerc 2.11
from datetime import date
print("Algoritmo que informa se o usuário é maior de idade")

ano_nascimento = int(input("Em qual ano você nasceu(aaaa): "))
ano = date.today().year
maioridade = True if ano - ano_nascimento >= 18 else False 

print(f" O usuário é maior de idade? {"verdadeiro" if maioridade else "falso"}")