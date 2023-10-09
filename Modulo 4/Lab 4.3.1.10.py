'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 07 de Octubre 
 Description:
 Laboratorio: 4.3.1.10
'''
def liters_100km_to_miles_gallon(liters):
    # 1 milla = 1609.344 metros, 1 km = 0.621371 millas, 1 galón = 3.785411784 litros
    return 100 / (liters / 3.785411784 * 0.621371)

def miles_gallon_to_liters_100km(miles):
    # 1 milla = 1609.344 metros, 1 km = 0.621371 millas, 1 galón = 3.785411784 litros
    return 100 / (miles * 1.609344 / 3.785411784)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
