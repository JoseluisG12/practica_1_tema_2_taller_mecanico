
class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { 1:self.op1,
                            2:self.op2,
                            3:self.op3,
                            4:self.op4,

        }

    def run(self,Clientes,Reparaciones):
        band = True
        while band:
            b = int(input("""
Menu pincipal:
1- para buscar a un cliente segun dni y listar sus reparaciones
2-determinar las reapraciones de un cliente por su patente
3-listar clientes a los que no le an terminado las reparaciones
4- para saber los datos de los clientes con mas de un vehiculo en reparacion
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(Clientes,Reparaciones)
            else:
                print("saliendo..")
                band = False


    def op1(self,Clientes,Reparaciones):
        patente = Clientes.buscardni()
        if patente != None:
            Reparaciones.listarpatente(patente)
        else:
            print("error no se encontro vehiculo registrado")

    def op2(self,Clientes,Reparaciones):
        patente = input("ingrese la patente a buscar\n")
        total = Reparaciones.buscarpatente(patente)
        if total == None:
            print("el vehiculo aun necesita reparaciones")
        else:
            Clientes.estado(patente)
            print("""
            TOTAL A PAGAR: ${}""".format(total))

    def op3(self,Clientes,Reparaciones):
        lista = []
        lista = Clientes.reparacionespendientes()
        for cliente in lista:
            print("""
DNI: {}                Apellido y nombre: {} {}
Patente: {}            Vehículo: {}""".format(cliente.getdni(),cliente.getapellido(),cliente.getnombre(),cliente.getpatente(),cliente.getvehiculo()))
            Reparaciones.listarreparaciones(cliente.getpatente())

    def op4(self,Clientes,Reparaciones):
        Clientes.masdeunvehiculo()







