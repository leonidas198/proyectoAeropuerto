# Leonidas

# from list import sort as ordenar  

def agregar_vuelo(vuelos, numero_vuelo, destino, hora_salida):
    vuelos[numero_vuelo] = {"destino": destino, "hora_salida": hora_salida}

# la llave y su valor son el mismo y su eleccion es para recordar sobre 
# que valores se trabaja.

def actualizar_hora_salida(vuelos, numero_vuelo, nueva_hora_salida):
    vuelos[numero_vuelo]["hora_salida"] = nueva_hora_salida

def ver_vuelos(vuelos):
    for numero_vuelo in vuelos:
        print(f"Vuelo {numero_vuelo}: Destino - {vuelos[numero_vuelo]['destino']}, Hora de Salida: {vuelos[numero_vuelo]['hora_salida']}")

vuelos = {}
agregar_vuelo(vuelos, "251", "Los Angeles", "08:00")
agregar_vuelo(vuelos, "312", "Japon", "12:35")
agregar_vuelo(vuelos, "588", "Rio de Janeiro", "11:15")
actualizar_hora_salida(vuelos, "251", "10:00")
ver_vuelos(vuelos)

# TO DO: No se puede importar la funcion sort porque ya es incorporada a la clase list de Phyton.


