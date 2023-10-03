'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.2.1.14 
'''

# Solicita al usuario que ingrese la cantidad de bloques
blocks = int(input("Ingresa el número de bloques: "))

# Inicializa variables
height = 0  # Altura de la pirámide
layer_blocks = 1  # Bloques requeridos para la capa actual
current_layer = 1  # Capa actual

# Calcula la altura de la pirámide
while blocks >= layer_blocks:
    height += 1
    current_layer += 1
    layer_blocks += current_layer

# Imprime la altura de la pirámide
print("La altura de la pirámide:", height)