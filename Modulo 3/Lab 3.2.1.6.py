'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.2.1.6
'''

import time

# Función para imprimir el mensaje final
def mensaje_final():
    print("¡Listos o no, ahí voy!")

# Bucle for que cuenta hasta cinco
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

# Llamar a la función de mensaje final después de contar hasta cinco
mensaje_final()