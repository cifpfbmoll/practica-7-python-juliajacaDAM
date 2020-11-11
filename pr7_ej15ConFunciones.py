'''
Desarrolla un programa utilizando la metodología “pair programming”,
que nos sirva para gestionar nuestros contactos 
(la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico.
El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave,
consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
(diccionarios, funciones, procedimientos…).
'''

def imprimirMenu():
    print('Bienvenida a su agenda, ¿Qué quieres hacer?')
    opcion = input('''
    Escribe '1' para añadir un contacto: 
    Escribe '2' para consultar un contacto buscando por el teléfono: 
    Escribe '3' para consultar todos los contactos: 
    Escribe '4' para borrar un contacto: 
    Escribe 'salir' para cerrar la agenda: 
    ''')
    return opcion


def introducirRegistro(diccionario, telefono, nombre, apellido1, apellido2, correo):
    diccionario[telefono] = {
            'nombre' : nombre,
            'apellido1' : apellido1,
            'apellido2': apellido2,
            'correo': correo
        }
def buscarContacto(diccionario, busqueda):
    diccionario_contacto =  diccionario[busqueda].items()
    for  tupla in diccionario_contacto:
        print(f'{tupla[0]}: {tupla[1]}')

def mostrarTodo(diccionario):
    for llave, valor in diccionario.items():
        print('--------------------------------')
        print('teléfono: ' , llave)
        for llave2, dato in valor.items():
            print(llave2, ': ', dato)

def borrarContacto(diccionario, borrar):
    contacto_borrado = diccionario.pop(borrar)
    print('Has borrado estos datos')
    for llave2, dato in contacto_borrado.items():
        print(llave2, ': ', dato)

def imprimirContinuar():
    input('Pulsa cualquier tecla para continuar')
    print('--------------------------------')

agenda = {}
opcion = ''


while opcion != 'salir':
    
    opcion = imprimirMenu()

    if opcion == '1':
        print('Has elegido añadir un contacto')
        telefono = input('Escribe el numero de telefono')
        nombre = input ('Escribe el nombre')
        apellido1 = input('Escribe el primer apellido')
        apellido2 = input('Escribe el segundo apellido')
        correo = input('Escribe el correo electrónico')

        introducirRegistro(agenda, telefono, nombre, apellido1, apellido2, correo)
        imprimirContinuar()

    elif opcion == '2':
        print('Vas a buscar un contacto por su teléfono')
        buscar = input('Escribe el teléfono a buscar: ')
        if buscar in agenda.keys():
            print('Contacto encontrado: ')
            buscarContacto(agenda, buscar)
        else : 
            print('NO se ha encontrado el contacto')

        imprimirContinuar()

    elif opcion == '3':
        print('Estos son tus contactos')
        print('--------------------------------')
        mostrarTodo(agenda)
        print('--------------------------------')
        imprimirContinuar()
    
    elif opcion == '4':
        print('Vas a borrar un contacto por su teléfono')
        borrar = input('Escribe el teléfono a borrar: ')
        if borrar in agenda.keys():
            print('Contacto encontrado: ')
            borrarContacto(agenda, borrar)
        else : 
            print('NO se ha encontrado el contacto')
        imprimirContinuar()
    
    elif opcion == 'salir':
        print('Gracias por usar tu agenda. Hasta pronto')
    
    else:
        print('No se reconoce esa instrucción, vuelve a intentarlo, por favor')
        imprimirContinuar()
