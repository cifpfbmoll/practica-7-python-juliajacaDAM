'''
Práctica 7 ejercicio 14
Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento,
que recibe como parámetro la fecha en números y devuelve la fecha con el nombre del mes.
Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 

'''
traducciones = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
 }
fecha = input('Introduce la fecha en formato dd/mm/yyyy, por ejemplo 01/01/2020: ')


def transformarFecha(fecha):
    listaNumeros = fecha.split('/') 
    mesLetra = traducciones[listaNumeros[1]]
    listaNumeros[1] = mesLetra
    print( f'La fecha es {listaNumeros[0] } de {listaNumeros[1]} de {listaNumeros[2]}')

transformarFecha(fecha)

