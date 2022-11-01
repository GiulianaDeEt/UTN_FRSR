# INDICE segundo semestre
# CLASE 1 → linea 20 (listas y tuplas)
# CLASE 2 → linea 122 (sets y diccionario)
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
Clase 1: listas
"""
# listas: conjunto de elementos, pueden contener cualquier tipo de dato.
# las listas tienen un índice. El primer elemento tiene índice 0.

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']  # dentro de una lista pueden haber distintos datos. Llevan []
print(nombres)
print(nombres[0])  # muestra el elemento del índice 0.
print(nombres[3])  # muestra el elemento del índice 3. En este ejemplo es el último
print(nombres[-1])  # cuando no sabemos cuántos elementos tiene la lista, con -1 mostraría el último, -2 el penúltimo...
# los índices positivos van de izquierda a derecha
# los índices negativos van de derecha a izquierda

# Recuperar rango de lista
print(nombres[0:2])  # recorrerá el índice desde el 0 hasta el 2 (no inclusive)

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])  # recorrerá desde el inicio del indice hasta el indice 3 (no inclusive)

# Desde el índice indicado hasta el final
print(nombres[1:])  # recorrerá a partir del indice 1 hasta el final

# Modificar un valor
nombres[2] = 'Liliana'  # modificamos el elemento del índice 2
nombres[0] = 'Natalia'  # modificamos el elemento del índice 0
print(nombres)

# Iterar una lista
for name in nombres:  # nombre es singular, la lista es plural
    print(name)
else:
    print("No hay mas nombres en la lista")

# Preguntar cuántos elementos tiene una lista
print(len(nombres))  # len devuelve un número dónde indica la cantidad de elemento en una lista

# Agregar un elemento a una lista
nombres.append('Marcelo')  # Agrega dicho elemento al FINAL de la lista
nombres.append([1, 2, 3])  # Una lista puede tener otra lista
nombres.append(True)  # Una lista puede tener un tipo boolean
nombres.append(10.45)  # Una lista puede tener un tipo float
nombres.append(7)  # Una lista puede tener un tipo inter
print(nombres)  # Todo en una misma lista

# Insertar un elemento en un índice específico
nombres.insert(1, 'Alberto')  # SI O SI se debe especificar el índice y luego el elemento a agregar
print(nombres)
nombres.insert(3, 'Debora')  # Agrega dicho elemento en el índice 3
print(nombres)

# Eliminar un elemento en una lista
nombres.remove('Alberto')  # Elimina dicho elemento
print(nombres)

# Eliminar el último elemento de una lista
nombres.pop()  # De esta manera elimina el último elemento de la lista
print(nombres)

# Eliminar un índice específico de una lista
del nombres[2]  # Elimina el elemento del dicho índice
print(nombres)

# Eliminar todos los elementos de una lista
nombres.clear()  # Limpia una lista. La lista se muestra así: []
print(nombres)

# Eliminar la lista
del nombres  # Elimina una lista por completo
# print(nombres) # Dará un error porque la lista ya no existe

# Las listas son MUTABLES, o sea, modificables. Las tuplas son INMUTABLES, o sea, no modificables

# Definir una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')  # Las tuplas llevan ()
print(len(cocina))

# Acceder a un elemento
print(cocina[0])  # Los índice SÍ se marcan con [] como en las listas
# Acceder a un elemento de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])  # Elementos desde el índice 0 hasta el índice 1 (sin incluir)

# ('papa') → es un string
# ('papa', ) → es una tupla. SÍ O SÍ necesita incluir la coma

# Recorrer los elementos de una tupla
for cocinar in cocina:
    # print(cocinar) # Print utiliza automáticamente el \n (salto de línea)
    print(cocinar, end=' ')  # Al finalizar el print, agrega un espacio en vez de salto de línea

# No se puede agregar un elemento nuevo a una tupla
cocina[0] = 'plato'
# print(cocina) # Mostrará un error porque las tuplas no son editables.

# ↓↓ ¡ESTO NO ES UNA BUENA PRÁCTICA! ¡EVITAR LO MÁXIMO POSIBLE! ↓↓

# ¿Cómo se podría editar una tupla? Pasando los elementos a una lista, modificar y volver a tupla
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)  # \n anula al end del anterior print.

# ↑↑ ¡ESTO NO ES UNA BUENA PRÁCTICA! ¡EVITAR LO MÁXIMO POSIBLE! ↑↑

"""
Clase 2: conjunto  o tipo set / diccionarios
"""
# Los tipos set no tienen un orden
# Los tipos set no permiten elementos duplicados o repetidos
# Los tipos set no se pueden modificar pero sí se puede agregar/eliminar
# Los tipos set no tienen índice, el orden es aleatorio

planetas = {'Marte', 'Júpiter', 'Venus'}  # Llevan llaves
print(planetas)  # Puede mostrar los elementos en distintos orden, por ej: {'Júpiter', 'Venus', 'Marte'}
print(len(planetas))  # Devuelve el largo del conjunto, osea, la cantidad de elementos

# Revisar si un elemento existe dentro de un set
print('Marte' in planetas)  # Boolean. Respeta mayúsculas, minúsculas y demás
print('Marte' not in planetas)

# Agregar un elemento
planetas.add('Mercurio')  # Agrega el elemento Mercurio al set
planetas.add('Mercurio')  # Como los sets no tienen elemento repetidos, éste elemento no aparece
print(planetas)

# Los tipos sets son MUY IMPORTANTES para casos en dónde se utilizan datos que no pueden ser duplicados

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Venus')  # Envía un error si el elemento no existe en el conjunto y detiene el programa
print(planetas)
planetas.discard('Jupiter')  # No envía un error, ni elimina nada, ni detiene el programa
print(planetas)

# Limpiar el set, eliminar todos sus elementos
planetas.clear()
print(planetas)

# Eliminar el set por completo
del planetas
print(planetas)  # Da un error si el conjunto ha sido eliminado correctamente

# DICCIONARIO
# Un diccionario está compuesto por 2 elementos
# Un diccionario está asociado a una llave y a un valor
# dict(key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',  # Importante colocar la , para agregar otro elemento
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'  # si es el último elemento, no hace falta la coma
}
print(diccionario)
print(len(diccionario))  # dice la cantidad de elementos que tiene el diccionario

# El diccionario es un tipo set, no tiene índice.
# Se accede al elemento a través de la key
# ¿Cómo acceder a un elemento?
print(diccionario['IDE'])  # Las key debe respetar la sintaxis
print(diccionario)  # devuelve: Integrated Development Environment

# Otra forma de acceder a un elemento, utilizando GET
print(diccionario.get('POO'))  # devuelve: Programación Orientada a Objetos

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'  # No modifica la key, modifica el value de la key ingresada
print(diccionario)

# ¿Cómo recorrer los elementos de un diccionario?
for termino in diccionario:
    print(termino)  # Muestra las key

for termino, valor in diccionario.items():  # Muestra las keys y sus valores. Si o si poner .items()
    print(termino, valor)

for termino in diccionario.keys():  # Otra forma de ver las keys
    print(termino)

for valor in diccionario.values():  # Muestra únicamente los valores sin las keys
    print(valor)

# Comprobar la existencia de un elemento en el diccionario
print('IDE' in diccionario)  # boolean
print('IDE' not in diccionario)

# Agregar un elemento al diccionario
diccionario['PK'] = 'Primary key'  # Se deben aclarar la Key y el value. No se repiten elementos
print(diccionario)

# Eliminar un elemento al diccionario
diccionario.pop('SABD')  # Se elimina tanto la key como su value
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario por completo
del diccionario
print(diccionario)

