"""
cargar por teclado y almacenar en una lista las alturas de 5 personas (valor float)
obtener el promedio de las mismas. contar cuantas personas son mas altas que el promedio
y cuantas mas bajas
"""

alturas = []
suma = 0

for i in range(5):
    altura = float(input(f"introduce la altura de la persona  {i+1} \n"))
    alturas.append(altura)
    suma = suma + altura
promedio = suma / 5
contador_mayor_promedio = 0
contador_menor_promedio = 0
for altura in alturas:

    if altura >= promedio:
        contador_mayor_promedio = contador_mayor_promedio +  1
    else:
        contador_menor_promedio = contador_menor_promedio + 1

print(f"hay {contador_mayor_promedio} persona con altura mayor al promedio y {contador_menor_promedio} personas con altura menor que el promedio")