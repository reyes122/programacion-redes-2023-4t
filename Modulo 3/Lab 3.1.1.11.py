'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.1.1.11
'''

income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
        tax = (income * (18/100)) - 556.2 
else:
        excedente = income - 85528
        tax = 14839.2 + (excedente * (32/100))
        
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
