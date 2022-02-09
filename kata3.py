# Ejercicios con if, elif, else
vasteroide = 49

if vasteroide > 25:
    print("Advertencia!  Vamos a morir!!!!")

velocidad = 19

if velocidad > 20:
    print("Puedes ver el rayo de luz del asteroide")
elif velocidad == 20:
    print("podemos morir pero no es 100% seguro")
else:
    print("Estamos a salvo, no puedes ver el rayo de luz")

#  Ejercicios con "and" y "or"

Dimension = 40
velocidad = 25

if Dimension>=25 and velocidad>=25:
    print("alerta!")
elif Dimension<25:
    print("Estamos a salvo")
elif velocidad>=20:
    print("Podemos ver una luz del asteroide")
else:
    print("Estamos a salvo") 
    

