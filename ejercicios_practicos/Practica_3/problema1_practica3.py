'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 09 de Octubre 
 Programacion de Redes
 Description:
 Laboratorio: 3.1.1.10
'''
# Creamos una lista vacía llamada 'datos' para almacenar los datos ingresados por el usuario.
datos = []

# Solicitamos al usuario ingresar 5 valores y los convertimos en enteros antes de agregarlos a la lista 'datos'.
for _ in range(5):
    datos.append(int(input()))

# Convertimos la lista 'datos' en una tupla llamada 'tuplaDatos'.
tuplaDatos = tuple(datos)

# Imprimimos los elementos de 'tuplaDatos'.
print("Elementos de tuplaDatos:")
for elemento in tuplaDatos:
    print(elemento)

# Imprimimos la longitud de la tupla 'tuplaDatos'.
print("Longitud de tuplaDatos:", len(tuplaDatos))

# Calculamos y luego imprimimos la suma de los elementos de 'tuplaDatos'.
suma = sum(tuplaDatos)
print("Suma de los elementos de tuplaDatos:", suma)

# Convertimos 'tuplaDatos' de nuevo en una lista llamada 'tuplaLista' y duplicamos el último elemento.
tuplaLista = list(tuplaDatos)
tuplaLista[-1] *= 2
tuplaDatos = tuple(tuplaLista)

# Imprimimos 'tuplaDatos' después de la modificación.
print("tuplaDatos después de duplicar el último elemento:", tuplaDatos)

# Calculamos y luego imprimimos el producto de los elementos de 'tuplaDatos'.
producto = 1
for elemento in tuplaDatos:
    producto *= elemento
print("Producto de los elementos de tuplaDatos:", producto)

# Creamos una tupla llamada 'tupla1' y calculamos una nueva tupla llamada 'tuplaSuma' que contiene la suma de elementos
# correspondientes de 'tuplaDatos' y 'tupla1'.
tupla1 = (1, 2, 3, 4, 5)
tuplaSuma = tuple(x + y for x, y in zip(tuplaDatos, tupla1))

# Imprimimos 'tuplaSuma'.
print("Resultado de la suma de tuplaDatos y tupla1:", tuplaSuma)

