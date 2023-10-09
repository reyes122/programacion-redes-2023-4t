'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 07 de Octubre 
 Description:
 Laboratorio: 4.3.1.6
'''

def is_year_leap(year):
    # Un año es bisiesto si es divisible por 4.
    # Sin embargo, los años divisibles por 100 no son bisiestos, a menos que también sean divisibles por 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")