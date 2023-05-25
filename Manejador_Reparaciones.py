from Clase_Reparaciones import Reparacion
import csv
import math
class Lista_de_Reparaciones:
    __reparaciones : list

    def __init__(self):
        self.__reparaciones = []

    def cargadatos(self):
        archivo = open('reparaciones.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        for fila in reader:
            patente = fila[0]
            repacion = fila[1]
            precioRepuesto = fila[2]
            precioManoDeObra = fila[3]
            estado = fila[4]
            reparacion = Reparacion(patente,repacion,precioRepuesto,precioManoDeObra,estado)
            self.__reparaciones.append(reparacion)

        archivo.close()


    def listarpatente(self,patente):
        print("""
Reparación                              precio del repuesto                        mano de obra                        subtotal""")
        total = 0
        for reparacion in self.__reparaciones:
            if reparacion.getpatente() == patente:
                print("""
{}                   ${}                                ${}                              ${}""".format(reparacion.getreparacion(),reparacion.getprecio(),reparacion.getmanodeobra(),reparacion.subtotal()))
                total = total +  reparacion.subtotal()

        print("""
                                                                          TOTAL A PAGAR ${} 
""".format(total))

    def buscarpatente(self,patente):
        resultado = 0
        total = 0
        for reparacion in self.__reparaciones:
            if reparacion.getpatente() == patente:
                total = total + reparacion.subtotal()
                if reparacion.getestado() == 'P':
                    resultado = None
        if resultado == None:
            return None
        else:
            return total


    def listarreparaciones(self,patente):
        print("""
Reparacion:""")
        for reparaciones in self.__reparaciones:
            if reparaciones.getpatente() == patente:
                if reparaciones.getestado() == 'P':
                    print("""
{}""".format(reparaciones.getreparacion()))







