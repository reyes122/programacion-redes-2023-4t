'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.1.1.12
'''

year = int(input("Introduce un año:"))
if year >= 1582:
    if year % 4 != 0:
        print("Año Comun")
    elif year % 100 != 0:
        print("Año Bisiesto")
    elif year % 400 != 0:
        print("Año Comun")
    else:
        print("Año Bisiesto")
else:
    print("No dentro del período del calendario Gregoriano")
