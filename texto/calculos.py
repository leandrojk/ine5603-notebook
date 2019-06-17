# arquivo calculos.py

# função que encontra o menor de três números
def menor_de_tres(numero1, numero2, numero3):
    menor_numero = numero1
    if numero2 < menor_numero:
        menor_numero = numero2
    if numero3 < menor_numero:
        menor_numero = numero3
    return menor_numero