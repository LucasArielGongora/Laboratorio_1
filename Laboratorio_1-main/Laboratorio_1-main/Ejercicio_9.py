# Ejercicio 9:
# Dadas las siguientes listas:
# y considerando que la posición en la lista corresponde a la misma persona,
# mostar el nombre de la persona más joven

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

edad_mas_joven = edades[0]
nombre_mas_joven = nombre[0]

for indice in range(len(edades)):
    if edades[indice] < edad_mas_joven:
        edad_mas_joven = edades[indice]
        nombre_mas_joven = nombre[indice]

print(f"La persona más joven es {nombre_mas_joven} con {edad_mas_joven} años.")
