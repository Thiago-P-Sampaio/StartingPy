#Exerc 8
print("============= Algoritmo de verificação de saldo bancário ============= ")
saldo = 500
while True:
     sacar = int(input(f" O usuário possui um saldo de R${saldo}, deseja sacar: \n 1. Sim \n 2. Não \n "))
     match sacar:
          case 1:
               valor = float(input("Digite o valor que deseja sacar "))
               if valor > saldo:
                    print("Transação não liberada, valor supera o saldo")
               else:
                    saldo -= valor
                    print(f"Transação liberada. Saldo disponível R${saldo}")
            
          case 2:
               break
                    