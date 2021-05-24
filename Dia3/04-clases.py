class Mueble:
    tipo=""
    valor=00.00
    colores=[]
    especificaciones=[]
    def indicar_tipo(self):
        return self.tipo
    def mostrar_especificaciones(self):
        self.indicar_tipo()
      #  print(Mueble.especificaciones)
       # print(self.especificaciones)
        return self.especificaciones
    

#para crear la instancia de la clase 
objeto_mueble=Mueble()
otro_mueble=Mueble()

objeto_mueble.especificaciones.append({"PAIS_PROCEDENCIA":"PERU"})
otro_mueble.especificaciones.append({"COLECCION":"VERANO"})

print(objeto_mueble.mostrar_especificaciones())
print(otro_mueble.mostrar_especificaciones())