# es la forma para evitar que los programas se CRASHEEN se caigan
try:
    print(10/2)
except ZeroDivisionError:
    print("No se puede dividir entre CERO")
except ValueError:
    print("Ingrese valor")
except:
    print("Algo salio mal")
else:
    print("Todo bien")
finally:
    print("Se ejecuta si o si")

#
numeros=[]
for numero in range(1, 5):
        try:
            numero_ingresado=int(input("Ingrese numero {} : d".format(numero)))
            numeros.append(numero_ingresado)
        except:
            print("Valor  incorrecto")

print("los numeros ingresados son:", numeros)