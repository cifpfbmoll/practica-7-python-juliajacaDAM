'''
Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while,
por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera 
(con for y sin breaks), o de otra (con while). Ambas funciones devolverá true (si es primo) 
o false (si no es primo). El programa principal informará del resultado. 
Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. 
Comentario: aprovecha el código que tienes ya creado
'''
import datetime

print('Averigua si tu número favorito es primo o no (Tiene que ser mayor de 1')
numero= int(input('Escribe aquí el número '))

def calcularPrimoConFor(numero):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True


def calcularPrimoConWhile(numero):
    divisor = 2
    while numero > divisor:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

h1 = datetime.datetime.now()
resultadoFor = calcularPrimoConFor(numero)
print(f'El número {numero} es primo') if resultadoFor else print(f'El número {numero} no es primo')
h2 = datetime.datetime.now()
tiempoFor = h2-h1
print('El tiempo del for ha sido' , tiempoFor)

h3 = datetime.datetime.now()
resultadoWhile = calcularPrimoConWhile(numero)
h4 = datetime.datetime.now()
print(f'El número {numero} es primo') if resultadoWhile else print(f'El número {numero} no es primo')
tiempoWhile = h4-h3
print('El tiempo del while ha sido' , tiempoWhile)