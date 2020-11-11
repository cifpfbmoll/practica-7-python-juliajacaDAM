'''
Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento,
y éste debe mostrar la frase con un carácter en cada línea.
'''

frase = 'Esta es mi frase de prueba.'

def mostrarUnCaracter(texto):
    for caracter in texto:
        print(caracter)

mostrarUnCaracter(frase)