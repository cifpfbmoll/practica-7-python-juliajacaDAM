'''
Práctica 7 Ejercicio 8
Escribe un programa que pida una frase (entrada por teclado), y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.
'''

frase = input('Escribe aquí tu frase: ')

def eliminarEspaciosBlanco(texto):
    return texto.replace(' ','')

print(eliminarEspaciosBlanco(frase))