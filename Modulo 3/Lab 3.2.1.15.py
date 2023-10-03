'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.2.1.15
'''

# Solicitar al usuario que ingrese un número natural
c0 = int(input("Ingresa un número natural: "))
pasos = 0

# Ejecutar la hipótesis de Collatz hasta que c0 sea igual a 1
while c0 > 1:
    c0 = (c0 // 2) if (c0 % 2 == 0) else (3 * c0 + 1)
    pasos += 1
    print(c0)

# Imprimir el número de pasos necesarios
print("Número de pasos necesarios:", pasos)