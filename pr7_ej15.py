'''
Desarrolla un programa utilizando la metodología “pair programming”,
que nos sirva para gestionar nuestros contactos 
(la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico.
El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave,
consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
(diccionarios, funciones, procedimientos…).
'''
agenda = {}
opcion = ''

while opcion != 'salir':
    print('Bienvenida a su agenda, ¿Qué quieres hacer?')
    opcion = input('''
    Escribe '1' para añadir un contacto: 
    Escribe '2' para consultar un contacto buscando por el teléfono: 
    Escribe '3' para consultar todos los contactos: 
    Escribe '4' para borrar un contacto: 
    Escribe 'salir' para cerrar la agenda: 
    ''')

    if opcion == '1':
        print('Has elegido añadir un contacto')
        telefono = input('Escribe el numero de telefono')
        nombre = input ('Escribe el nombre')
        apellido1 = input('Escribe el primer apellido')
        apellido2 = input('Escribe el segundo apellido')
        correo = input('Escribe el correo electrónico')
        agenda[telefono] = {
            'nombre' : nombre,
            'apellido1' : apellido1,
            'apellido2': apellido2,
            'correo': correo
        }
        input('Pulsa cualquier tecla para continuar')
        print('--------------------------------')

    elif opcion == '2':
        print('Vas a buscar un contacto por su teléfono')
        buscar = input('Escribe el teléfono a buscar: ')
        if buscar in agenda.keys():
            print('Contacto encontrado: ')
            # print(agenda[buscar].items())
            diccionario_contacto =  agenda[buscar].items()
            for  tupla in diccionario_contacto:
                print(f'{tupla[0]}: {tupla[1]}')
        else : 
            print('NO se ha encontrado el contacto')
        input('Pulsa cualquier tecla para continuar')
        print('--------------------------------')

    elif opcion == '3':
        print('Estos son tus contactos')
        print('--------------------------------')
        for llave, valor in agenda.items():
            print('--------------------------------')
            print('teléfono: ' , llave)
            for llave2, dato in valor.items():
                print(llave2, ': ', dato)
        print('--------------------------------')
        input('Pulsa cualquier tecla para continuar')
        print('--------------------------------')
    
    elif opcion == '4':
        print('Vas a borrar un contacto por su teléfono')
        borrar = input('Escribe el teléfono a borrar: ')
        if borrar in agenda.keys():
            print('Contacto encontrado: ')
            contacto_borrado = agenda.pop(borrar)
            print('Has borrado estos datos')
            for llave2, dato in contacto_borrado.items():
                print(llave2, ': ', dato)

            input('pulsa cualquier tecla para continuar')
            print('--------------------------------')
        else : 
            print('NO se ha encontrado el contacto')
            input('Pulsa cualquier tecla para continuar')
            print('--------------------------------')
    
    elif opcion == 'salir':
        print('Gracias por usar tu agenda. Hasta pronto')
        print('--------------------------------')
    
    else:
        print('No se reconoce esa instrucción, vuelve a intentarlo, por favor')
        input('Pulsa cualquier tecla para continuar')
        print('--------------------------------')
