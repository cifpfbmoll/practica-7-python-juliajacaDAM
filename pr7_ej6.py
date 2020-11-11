'''
Prçactica 7 ejercicio 6
Escribe un programa que lea el nombre de una persona y un carácter (entrada por teclado), le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.
'''

nombre = input('Escribe tu nombre: ')
caracter = input('Escribe un caracter: ')

def estaCaracter(nombre, caracter):
    if caracter.lower() in nombre.lower():
        return True
    return False

resultado = estaCaracter(nombre, caracter)

print(f'El caracter {caracter} está en el nombre {nombre}') if resultado else print(f'El caracter {caracter} no está en el nombre {nombre}')