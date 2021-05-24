# Variable LISTA
colores=['azul','negro','amarillo','purpura']
misc=['Eduardo',18,False,14.5,'1981-11-06',['1',2]]

print(colores)
print(colores[1])
print(colores[len(colores)-1])
print(colores[-1])
print(colores[0:2])
print(colores[1:])
# Copiand contenido sin usar la misma posicion de memoria
colores2=colores[:]
colores2[0]='maron'
print(colores)
print(colores2)

colores.append('rojo')
print(colores)
colores.remove('azul')
print(colores)
colores.pop(0)

colores.clear()
#tuplas
notas=(14,16,17,11,5,5,5,5,1)
print(notas[0])
print(f"Cantidad de elementos {len(notas)}")
print("Cantidad de elementos {}". format(len(notas)))
#ver elemntos repetidos en la TUPLA
print( notas.count(5))
# conjunto => coleccion de elementos desordenados
estaciones={"Verano","Invierno","Otoño","Primavera"}
print(estaciones)
estaciones.add("Otono-Verano")
print(estaciones)
print("Otono-Verano" in estaciones)

# Diccionarios => coleccion de elementos que estan indexados, que nosotros manejamos el nombre de la llave
persona = {
    "id":"1",
    "nombre":"Carlos",
    "relacion":"casado",
    "hobbies":[
        {
            "nombre":"futbol",
            "conocimiento":"bueno"
        },
         {
            "nombre":"voley",
            "conocimiento":"nada"
        }
    ]
}

print(persona['nombre'])
print(persona['hobbies'] [0] ["conocimiento"]  )
persona["apellido"]="Ayala"
print(persona)


libro = {
    "nombre": "Harry Potter",
    "autor": "J.K. Rowling",
    "editorial": "Blablabla",
    "año": 2018,
    "idiomas": [
        {
            "nombre": "portuges"
        },
        {
            "nombre": "ingles",
            "nombre": "ingles britanico"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
    "tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix")
}


print(libro["autor"])
print(libro['tomos'] [1] )
print(len(libro))
print("Ruso" in libro["idiomas"])



