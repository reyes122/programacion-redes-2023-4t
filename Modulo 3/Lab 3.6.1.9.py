'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.6.1.9
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]


unique_list = []


for num in my_list:
    
    if num not in unique_list:
        unique_list.append(num)


print("La lista con elementos únicos:")
print(unique_list)

