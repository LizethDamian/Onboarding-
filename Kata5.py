#Ejercicio 1 Operador aritmetico 

tierra = 149597870
jupiter = 778547200

distanciakm = jupiter - tierra
kmamillas = distanciakm*0.621

print(f'La distancia en kilometros es: {distanciakm} \n La distancia en millas es {kmamillas}')

#Ejercicio 2 Convierte cadenas en numeros y usa valores absolutos 

nombreusuario = input('¿Cual es tu nombre?  ')
primerplaneta = input('Favor de ingresar el nombre del primer planeta: ')
primerdistancia = input('Favor de ingresar la distancia al sol del primer planeta: ')
segundoplaneta = input('Favor de ingresar el nombre del segundo planeta: ')
segundodistancia = input('Favor de ingresar la distancia al sol del segundo planeta: ')

distanciauno = int(primerdistancia)
distanciados = int(segundodistancia)

diferencia = abs(distanciauno-distanciados)
millas = diferencia*0.621
print(f'La distancia es: {diferencia} en km')
print(f'La distancia en millas es: {millas}')

