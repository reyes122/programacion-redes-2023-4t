'''
 Nombre: Bryan Adrian Reyes Ibarra
 Fecha: 25 DE Septiembre 
 Description:
 Laboratorio: 2.6.1.11
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

salida = (hour + (mins + dura) // 60)% 24
salidamn = (mins + dura)% 60

print(salida,salidamn,sep=":")
