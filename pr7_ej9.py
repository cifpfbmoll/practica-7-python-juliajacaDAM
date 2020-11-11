'''
Práctica 7 ejercicio 9
Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman
'''

palabra1 = input('escribe la primera palabra: ')
palabra2 = input('escribe la segunda palabra: ')

def comprobarRima(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        print(f'Las palabras {palabra1} y {palabra2} riman muy bien')
    elif palabra1[-2:] == palabra2[-2:]:
        print(f'Las palabras {palabra1} y {palabra2} riman un poco')
    else: 
        print(f'Las palabras {palabra1} y {palabra2} no riman nada')

comprobarRima(palabra1, palabra2)