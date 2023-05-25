import  csv
from Clase_Cliente import Cliente
class Lista_de_Clientes:
    __Clientes : list

    def __init__(self):
        self.__Clientes = []


    def cargadatos(self):

        archivo = open('clientes.csv')
        reader =  csv.reader(archivo,delimiter=(';'))
        next(reader)
        for fila in reader:
            dni = fila[0]
            apellido = fila[1]
            nombre = fila[2]
            telefono = fila[3]
            patente = fila[4]
            vehiculo = fila[5]
            estado = fila[6]
            cliente = Cliente(dni,apellido,nombre,telefono,patente,vehiculo,estado)
            self.__Clientes.append(cliente)

        archivo.close()

    def buscardni(self):
        dni = int(input('ingrese el dni del cliente a buscar\n'))
        band = True
        i = 0
        while band != False and i < len(self.__Clientes):

            if self.__Clientes[i].getdni() == dni:
                band = False
            else:
                i = i + 1

        if i < len(self.__Clientes):
            print("""
DNI: {}                Apellido y nombre: {} {}
Patente: {}            Vehículo: {}""".format(self.__Clientes[i].getdni(), self.__Clientes[i].getapellido(),self.__Clientes[i].getnombre(),self.__Clientes[i].getpatente(),self.__Clientes[i].getvehiculo()))
            return self.__Clientes[i].getpatente()
        else:
            return None


    def estado(self,patente):
        band = True
        i = 0
        while band and i < len(self.__Clientes):
            if self.__Clientes[i].getpatente() == patente:
                self.__Clientes[i].modificaestado()
                print("""
Trabajo terminado 
cliente: {} {} 
telefono: {}
 vehiculo: {}""".format(self.__Clientes[i].getapellido(),self.__Clientes[i].getnombre(),self.__Clientes[i].gettelefono(),self.__Clientes[i].getvehiculo()))
                band = False
            else:
                i = i + 1


    def reparacionespendientes(self):
        lista = []
        for cliente in self.__Clientes:
            if cliente.getestado() == 'P':
                lista.append(cliente)
        return lista

    def masdeunvehiculo(self):
        for i in range(len(self.__Clientes)):
            b = 0

            while  b < len(self.__Clientes):
                if (id(self.__Clientes[i]) != id(self.__Clientes[b])):
                    if self.__Clientes[i] == self.__Clientes[b]:
                        print("""
Cliente con mas de un vehiculo en reparacion:
Cliente: {} {}
DNI:{}
telefono:{}
patente:{}
vehiculo:{}""".format(self.__Clientes[i].getapellido(),self.__Clientes[i].getnombre(),self.__Clientes[i].getdni(),self.__Clientes[i].gettelefono(),self.__Clientes[i].getpatente(),self.__Clientes[i].getvehiculo()))
                        b = b + 1
                    else:
                        b = b + 1


                else:
                    b = b + 1


