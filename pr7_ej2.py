'''
Práctica 7 ejercico 2
Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes),
los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena.
La cadena final la imprimirá el programa por pantalla.
'''

nombrePersona = 'Perico'
apellido1Persona = 'Palotes'
apellido2Persona = 'Palotes'

def unirNombreApellidos(nombre, apellido1, apellido2):
    return (f'{nombre} {apellido1} {apellido1}')

nombreCompleto = unirNombreApellidos(nombrePersona, apellido1Persona, apellido2Persona)
print(nombreCompleto)