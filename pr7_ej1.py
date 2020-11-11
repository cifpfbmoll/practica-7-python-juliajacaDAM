'''
Práctica 7 Ejercicio 1
Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento,
y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
'''

textoUsuario = input('Escribe aquí tu texto: ')

def ponerMayusculasMinusculas(texto):
    print(texto.lower())
    print(texto.upper())

ponerMayusculasMinusculas(textoUsuario)