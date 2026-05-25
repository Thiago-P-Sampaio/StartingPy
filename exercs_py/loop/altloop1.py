lista_de_numeros = [12, 15, 7, 9, 27, 34]
n = int(input('Digite o número a procurar:'))

for x in range(len(lista_de_numeros)):
        if lista_de_numeros[x] == n:
            break
        x += 1
        
if x < len(lista_de_numeros):
    print(f"{n} achado na posição {x}")
else:
    print(f"{n} não encontrado")