# INDICE segundo semestre
# CLASE 1 → linea 20
# CLASE 2 → linea
# CLASE 3 → linea
# CLASE 4 → linea
# CLASE 5 → linea
# CLASE 6 → linea
# CLASE 7 → linea
# CLASE 8 → linea
# CLASE 9 → linea
# CLASE 10 → linea
# CLASE 11 → linea
# CLASE 12 → linea
# CLASE 13 → linea
# CLASE 15 → linea
# CLASE 16 → linea
# CLASE 17 → linea

"""
Clase 1
Sintaxis de range(inicio <opcional>, fin <requerido>, incremento <opcional>)
"""

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo de ejecución: 0,3,6,9

print ('Rango de 0 a 10 con números divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de números de 2 a 6, imprimir
# Ejemplo de ejecución: 2,3,4,5,6

print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print(i)

# Ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9

print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
for i in range(3,11,2):
    print(i)

# Ejercicio 4: dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1 ,3 ,2]

lista = []  # Definimos una lista vacía
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)


# --------------------------------------------------------------------------------------------
def cels_fahr(grados_celsius):
    return (grados_celsius * 9 / 5) + 32


# De fahrenheit a celsius:
def fahr_cels(grados_fahrenheit):
    return (grados_fahrenheit - 32) * 5 / 9


celsius = float(input('Ingrese un temperatura en grados celsius: '))
resultadoCF = cels_fahr(celsius)
print(f'{celsius}°C a F → {resultadoCF:.2f}F')

fahrenheit = float(input('Ingrese un temperatura en fahrenheit: '))
resultadoFC = fahr_cels(fahrenheit)
print(f'{fahrenheit}F a °C → {resultadoFC:.2f}°C')