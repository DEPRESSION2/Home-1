from random import randint as rand

number_of_cars = 5

brands = [
"BMW",
"Mercedes",
"Toyota",
"Audi",
"Lamborgini",
"Chevrolet",
"Nissan",
"Hyndai",
"Ford",
"Honda"
]

models = [
 ['x5', 'x6', 'm3', 'i8', 'e39'],
 ['GL350', 'SLK', 'Maybach', 'Brabus', 'S600'],
 ['Land Cruser', 'Supra', 'Hilander', 'Avalon', 'RAV4'],
 ['s6', 'a1', 'a5', 'a7', 'q7'],
 ['SVG', 'Aventador', 'Galarda', 'Hurakan', 'Diablo'],
 ['Aveo', 'Camaro', 'Traverse', 'Lachetti', 'Volt'],
 ['Silvia', 'Rogue', 'Juke', 'GTR', 'Leaf'],
 ['Sonata', 'Santa Fe', 'Elantra', 'i30', 'i20'],
 ['Focus', 'Explorer', 'Expedition', 'Fusion', 'Fiesta'],
 ['CRV', 'Civic', 'CRZ', 'Jazz', 'Accord']
]


import random
for i in range(5):
	b = random.randint(0, 1)
	print('I have',brands[b], models[b][random.randint(0, 4)])
	l = list(range(5)(print('I have',brands[b], models[b][random.randint(0, 4)])))
	print(l)

for i in range(5):
	b = random.randint(0, 1)