#==  es igual que
# ≠ es difernete 
#< , > menor que , mayor que 
# ≤ , ≥ menor igual que alt+243 , mayor igual que alt+242

numero1, numero2= 10 ,20

print(numero1 < numero2)

print( (10 > 5) and (10 > 11) )

print( (10 >= 5) or  (10 > 20) )

print( not(10 >= 5) or  (10 > 20) )

# is => es 
# is not => no es

# variable MUTABLES y las INMUTABLES
# Mutable = se almacenan en el mismo espacio de memoria
nombre=['Eduardo','Raul','Carlos','Estefani']
nombre_alumnos=nombre
nombre_alumnos[0]='Carmen'
print(nombre)

nacionalidad='Ecuatoriana'
nacionalidad2='Peruana'
# id se usa para identicar la posicion de memoria de la variable
print(id(nombre))
