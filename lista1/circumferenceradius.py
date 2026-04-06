#Exerc 2.9
import math

print("Algoritmo que calcula área da circunfêrencia: ")
pi =  round(math.pi,2)

raio = float(input("Informe o raio da circunfêrencia(cm): "))

area = pi*(raio**2)

print(f"A área da circunferência é {area:.2f} cm2, dado PI: {pi}")


