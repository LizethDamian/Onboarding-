# EJERCICIO 1 TRANSFORMAR CADENAS

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highe The highest daylight temperature of the Moon is 127 C."""

divisiontext = text.split(". ")
divisiontext

PalabrasC = ["average", "temperature", "distance"]

for texto in divisiontext:
    for PalabrasC in PalabrasC:
        if PalabrasC in texto:
            print(texto)
            break

print("-"*60)

for texto in divisiontext:
    for PalabrasC in PalabrasC:
        if PalabrasC in texto:
            print(texto.replace(' C', ' Celsius'))
            break  

print("-"*60)

# EJERCICIO 2 FORMATEANDO CADENAS

# Datos con los que vas a trabajar
gravity = 0.00162 #En km
planillaluna= """Name = "Moon"
Gravity = 0.00162 
Planet = "Earth" """

titulo = "Gravedad en la tierra y en la luna"
print(titulo.title())

print("-"*60)
print(planillaluna)
print('\n')
gravedad = gravity*1000
print("La gravedad en metros es: ", gravedad)

print("-"*60)

gravity = 0.00143
nuevaplanilla= """Name = "Ganimedes"
Gravity = 0.00143 
Planet = "Marte" """


print(nuevaplanilla)
print("La gravedad en metros es:", gravity*1000)









