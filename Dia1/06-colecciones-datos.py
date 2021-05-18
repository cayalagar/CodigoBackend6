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
