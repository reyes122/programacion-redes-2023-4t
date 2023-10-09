'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 07 de Octubre 
 Description:
 Laboratorio: 4.3.1.8
'''

def is_year_leap(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si los argumentos tienen sentido.
    if month < 1 or month > 12 or year < 1:
        return None

    # Ajustar febrero para años bisiestos.
    if is_year_leap(year) and month == 2:
        return 29

    # Devolver el número de días correspondiente al mes.
    return days_per_month[month]

def day_of_year(year, month, day):
    # Verificar si los argumentos son válidos.
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Calcular el día correspondiente del año.
    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)
    
    return day_count


print(day_of_year(2000, 12, 31))  
print(day_of_year(2023, 4, 15))   