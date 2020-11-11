'''
Práctica 7 ejercicio 5
Escribe un programa que te pida una frase y una vocal (entrada por teclado), y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá:

'''

frase = input('Escribe aquí tu frase: ')
vocal = input('Escribe aquí tu vocal: ')
vocales = ('a','e','i', 'o', 'u')

def sustituirVocalesPorLetra(texto, letra):
    for caracter in texto:
        if caracter in vocales:
            texto = texto.replace(caracter, letra)           
    return texto

print(sustituirVocalesPorLetra(frase, vocal))