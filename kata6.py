
# Ejercicio 1 

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] 

print(f'Los planetas en el sistema solar son: {len(planets)} ')

planets.append('Pluton')

print(f'El numero de planetas son: {len(planets)}')
print('El ultimo planeta del sistema solar es:', planets[-1])

#Ejercicio 2

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
nombreP = input("Favor de ingresar el nombre de un planeta \n(recuerde ingresar la primera letra en mayuscula): ")

enontrarplaneta = planets.index(nombreP) #colocamos antes del punto la lista inicial y como argumento el nombre de la variable del usuario

print("Estos son los planetas mas cercanos al sol: " + nombreP) #se coloca + para unir las cadenas 
print(planets[0:enontrarplaneta]) #muestra a los planetas antes del que coloco el usuario

print("Estos son los planetas mas lejanos al sol: " + nombreP)
print(planets[enontrarplaneta:]) #Muestra los planetas despues del que coloco el usuario 