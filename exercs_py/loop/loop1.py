lista_de_numeros = [12,  15,  7,  9,  27, 34]
#índice            0º   1º   2º  3º  4º  5º
print("="*60)
num = int(input("Informe um número inteiro: "))
y = 0
for i in lista_de_numeros:
    existe = False # estado falso padrão
    if i == num:
        existe = True
        print("%d encontrado na posição %dº"% (num, y))
        break

    else:
        y += 1

if not existe: print("%d não existe na lista"% num)
        