'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.4.1.6
'''

# Lista existente de números ocultos en el sombrero.
hat_list = [1, 2, 3, 4, 5]

# Paso 1: Solicitar al usuario que reemplace el número central en la lista.
hat_list[2] = int(input("Ingresa un número entero para reemplazar el número central: "))

# Paso 2: Eliminar el último elemento de la lista.
hat_list.pop()

# Paso 3: Imprimir la longitud de la lista existente.
print("Longitud de la lista existente:", len(hat_list))

# Imprimir la lista modificada
print(hat_list)