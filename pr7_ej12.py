'''
Práctica 7 ejercicio 12
Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar 
el número de palabras que contiene. Debe imprimir el programa principal el resultado.
Asumir que cada palabra está separada por un solo blanco:
Asumir que cada palabra está separada por un solo blanco.
No se sabe cómo están separadas las palabras. Pueden estar separadas por más de un blanco o por signos de puntuación.

'''
import re

frase = input('Escribe aquí una frase: ')

def contarPalabras(texto):
    listaPalabras = re.split("\W", texto)
    return len(listaPalabras)        

resultado = contarPalabras(frase)

print(f'La frase tiene {resultado} palabras')
