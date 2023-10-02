'''
Autor: Bryan Adrian Reyes Ibarra
Fecha: 02 de Octubre 
Description: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% 
de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
segundo y tercer años. Redondear cada cantidad a dos decimales.
'''

inicial = float(input("Cantidad de Dinero Depositado: "))

for i in range(1,4):
    if i == 1:
        primer=  inicial + (inicial*(4/100))
        print("Cantidad de Ahorro Primer año: ",round(primer))
    elif i == 2:
        segundo=  primer + (primer*(4/100))
        print("Cantidad de Ahorro Segundo año: ",round(segundo))
    elif i == 3:
        tercero =  segundo + (segundo*(4/100))
        print("Cantidad de Ahorro Tercer año: ",round(tercero))
        