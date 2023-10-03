'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 02 de Octubre 
 Description:
 Laboratorio: 3.4.1.13
'''

beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for i in range (len(beatles)-2):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best") 
print("Paso 3:", beatles)

del beatles[4]
del beatles[3]
print("paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

print("Los Fav", len(beatles))