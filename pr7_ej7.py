'''
Práctica 7 ejercicio 7
Escribe un programa que lea una frase (entrada por teclado), y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.
'''

frase = input('Escribe aquí tu frase: ')

def contarVocales(texto):
    contador = 0
    vocales = ('a','e', 'i', 'o', 'u')
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    print(f'En el texto "{texto}" hay {contador} vocales')


contarVocales(frase)