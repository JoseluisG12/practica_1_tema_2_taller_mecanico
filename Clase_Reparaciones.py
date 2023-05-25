import math
class Reparacion:
    __patente : str
    __reparacion : str
    __precio_de_repuesto : float
    __precio_mano_de_obra : float
    __estado : str

    def __init__(self,patente,reparacion,repuesto,precio,estado):
        self.__patente =  patente
        self.__reparacion = reparacion
        self.__precio_de_repuestorepuesto = float(repuesto)
        self.__precio_mano_de_obra = float(precio)
        self.__estado = estado



    def getreparacion(self):
        return self.__reparacion

    def getprecio(self):
        return self.__precio_de_repuestorepuesto

    def getmanodeobra(self):
        return self.__precio_mano_de_obra

    def subtotal(self):
        return (self.__precio_de_repuestorepuesto + self.__precio_mano_de_obra)

    def getpatente(self):
        return self.__patente

    def getestado(self):
        return self.__estado

