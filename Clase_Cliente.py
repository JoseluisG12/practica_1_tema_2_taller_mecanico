
class Cliente:
    __dni : int
    __apellido : str
    __nombre : str
    __telefono : int
    __pantente : str
    __vehiculo : str
    __estado : str
    def __init__(self,dni,apellido,nombre,telefono,pantente,vehiculo,estado):
        self.__dni = int(dni)
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__pantente = pantente
        self.__vehiculo = vehiculo
        self.__estado = estado

    def getdni(self):
        return int(self.__dni)

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def getpatente(self):
        return self.__pantente

    def getvehiculo(self):
        return self.__vehiculo

    def gettelefono(self):
        return self.__telefono

    def getestado(self):
        return self.__estado

    def modificaestado(self):
        self.__estado = 'T'
    def __eq__(self, other):
        if self.__dni == other.__dni:
            if self.__nombre == other.__nombre:
                if self.__apellido == other.__apellido:
                    if self.__telefono == other.__telefono:
                        return True

                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

