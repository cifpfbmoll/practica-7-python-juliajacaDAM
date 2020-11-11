'''
Práctica 7 ejercicio 11
Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:
'''


frase = input('Escribe la palabra: ')

def esPalindromo(texto):
    ida = list()
    vuelta = list()

    for caracter in texto.replace(' ',''):
        ida.append(caracter)

    for caracter in texto[::-1].replace(' ',''):
        vuelta.append(caracter)

    if ida == vuelta:
        return True
    return False

resultado = esPalindromo(frase)

print(f'La frase "{frase}" es palindromo') if resultado else print(f'La frase "{frase}" no es palindromo')