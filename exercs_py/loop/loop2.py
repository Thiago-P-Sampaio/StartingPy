print("="*40, "\n")

lista1 = []
lista2 = []
lista3 = []

while True:
    num = int(input(f"Digite um número para lista, digite 0 para encerrar"))
    if num == 0: break
    lista1.append(num)
while True:
    num = int(input(f"Digite um número para uma segunda lista, digite 0 para encerrar"))
    if num == 0: break
    lista2.append(num)
    
for x in range(len(lista1)):
    lista3.append(lista1[x])
    if len(lista3) == len(lista1):
        for i in range(len(lista2)):
            if lista2[i] != lista3[i]: lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)

# for x in range(len(lista1) + len(lista2)): #Não precisa iterar sobre o tamanho de duas listas
#     lista3.append(lista1[x])  # A iteração vai continuar com índice fora do limite de lista1 dando erro
#     if len(lista3) == len(lista1):
#         if lista2[x] != lista3[x]: lista3.append(lista2[x])