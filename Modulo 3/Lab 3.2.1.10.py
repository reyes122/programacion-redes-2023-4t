﻿'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.2.1.10
'''

user_word = input("Ingresa una palabra: ")


user_word = user_word.upper()


for letter in user_word:
    
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue  
    else:
        print(letter)  