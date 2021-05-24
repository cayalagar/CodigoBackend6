"""
# ingresar datos por terminal
edad=input("Ingresa tu edad:")
print(type(edad))

edadEntero=int(edad)
print(type(edadEntero))

# \n => salto de linea
# \t => tabulacion
#Condicional IF, ELSE , ELIF
restricion_edad=18
if edadEntero > restricion_edad  and edadEntero<65:
        print("Eres mayo de edad, ya puede viajar") 
elif edadEntero>=65:
        print("Puedes ir aun crucero")
else :
    print("Eres menor de edad, no puede viajar")
#operador ternario
respuesta="Eres mayor de edad" if(edadEntero>=18) else "Eres menor de edad"
print(respuesta)


# ingresar datos por terminal

numero=input("Ingresa un numero:")
numeroCompara=int(numero)

if numeroCompara<0:
        print("Eres negativo") 
elif numeroCompara==0:
        print("Eres cero")
else :
    print("Eres positivo")
"""
#Bucles
# FOR
"""
meses=["enero","febrero","marzo","abril","mayo","junio"]

for mes in meses:
    print(mes)

for numero in range(0, 10,2):
    print(numero)


diccionario1={
      "nombre":"Eduardo",
      "apellido":"Martinez"
  }  

for llave in diccionario1:
      print(diccionario1[llave])
"""

numeros=[1,-4,5,-14,-16,-50,6,-100]

positivo=0
negativos=0
for valor in numeros:
    if  valor<0:
        negativos=negativos+1
    else:
        positivo=positivo+1

print(f"Hay {positivo} positivos y {negativos} negativos")

for i in range(10):
        print(i)
        if i==5:
            break

for i in range(10):
        if i==5:
            continue
        print(i)

grupoNumero=[1,2,5,9,12,15,10,34,867,67]      
#indicar cuantos de ellos son multiplos de 3 y de 5 ademas si hay un multiplo de 3 y de 5 no contar
multiplo3=0
multiplo5=0
for valor in grupoNumero:
    if valor % 3 ==0 and valor % 5 ==0:
        continue
    elif valor % 3 ==0:
        multiplo3=multiplo3+1
    elif valor % 5 ==0:
        multiplo5=multiplo5+1

print("Hay {} multiplos de 3, {} multiplos de 5".format(multiplo3,multiplo5))

# while
edad=25

while edad>18:
        print(edad)
        edad -=1

# ingresar por teclado 3 nombres e indicar cuantos pertencen a la siguiente lista
inscritos = ["raul", "pedro", "maria", "roxana", "margioret"]

nombre1=input("Primer nombre:")
nombre2=input("Segundo nombre:")
nombre3=input("Tercer nombre:")

for dato in inscritos:
    if dato==nombre1:
           print("{} pertenese a inscritos".format(dato))
    elif dato==nombre2:
           print("{} pertenese a inscritos".format(dato))
    elif dato==nombre3:
           print("{} pertenese a inscritos".format(dato))


for nombre in range(1, 4):
        nombre_ingresado=input("Ingrese nombre {}".format(nombre))
        if (nombre_ingresado in inscritos):
            print("Bienvenido(a) {}".format(nombre_ingresado))