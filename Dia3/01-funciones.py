#Funciones se reutilizan
def saludar():
    """Funcion que te saluda """
    print("Hola amigos buenas tardes")

#saludar()

def saludarConNombre(nombre):
    """Funcion que te saluda """
    print(f"Hola{nombre} buenas tardes ")

#saludarConNombre("Carlos")

def saludarOpcional(nombre=None):
    print(f"Hola como estas {nombre}")

#saludarOpcional()

# Parametros opcionales simepre al final de la funcion
def registro( correo, nombre=None):
    print("Registro exitoso")

#registro("cayala@hotmail.com")

# funcion que reciba 2 numeros y si la sumatoria es par indicar la mitas else mostrar
def sumatoriaRara(numero1, numero2):
    valor=numero1+ numero2
    if ((valor % 2 )==0):
        valor=valor/2

    print(valor)

#sumatoriaRara(6,3)

# * parametros ilimitados   ARGS
def inscritos(*args):
    print(args)

#inscritos("Eduardo","Jesus","Carlos","Ana","Brigitte")

# definir una funcion para que reciba una N cantidad de alumnos y que indique cuantos fueron aprobados y cuandos desaprobaron

def alumnos(*args):
    total=len(args)
    aprobados=0
    desapropbados=0
    for alumnos in args:
        nota=alumnos["nota"]
        if nota>10:
                aprobados +=1
        else:
                desapropbados +=1
    print(f"hay {aprobados}  aprobados y {desapropbados} de {total} alumnos")

alumnos({"nombre": "Eduardo", "nota": 7},
            {"nombre": "Fidel", "nota": 16},
            {"nombre": "Raul", "nota": 18},
            {"nombre": "Marta", "nota": 20},
            {"nombre": "Juliana", "nota": 14},
            {"nombre": "Fabiola", "nota": 16},
            {"nombre": "Lizbeth", "nota": 15})


def indeterminadoConNombre(**kwargs):
    print(kwargs)

indeterminadoConNombre(nombre="carlos",apellido="ayala",edad=18)

def multiplicacion(num1, num2):
    return num1*num2


resultado=multiplicacion(15,2)
print(resultado)