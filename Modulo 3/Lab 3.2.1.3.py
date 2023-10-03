'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.2.1.3
'''



secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
user_guess = input()

while True:
    try:
        
        if user_guess == secret_number:
            print("¡Bien hecho, muggle! Eres libre ahora.")
            break
        else:
            print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
