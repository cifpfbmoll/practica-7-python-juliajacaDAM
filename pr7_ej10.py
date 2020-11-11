'''
Práctica 7 ejercicio 10
Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:
'''

palabra1 = input('Escribe la palabra: ')

def esPalindromo(texto):
    ida = list()
    vuelta = list()

    for caracter in texto:
        ida.append(caracter)

    for caracter in texto[::-1]:
        vuelta.append(caracter)

    # print(ida)
    # print(vuelta)

    if ida == vuelta:
        return True
    return False


resultado = esPalindromo(palabra1)

print(f'La palabra {palabra1} es palindromo') if resultado else print(f'La palabra {palabra1} no es palindromo')