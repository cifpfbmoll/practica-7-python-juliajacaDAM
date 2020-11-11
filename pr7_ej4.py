'''
Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase.
La función debe sustituir todos los espacios en blanco de una frase por un asterisco,
y devolver el resultado para que el programa principal la imprima por pantalla.
'''

frase = input('Escribe aquí tu frase: ')

def sustituirEspaciosBlanco(texto):
    return texto.replace(' ','*')

print(sustituirEspaciosBlanco(frase))