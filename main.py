from Manejador_Reparaciones import Lista_de_Reparaciones
from Manejador_Cliente import  Lista_de_Clientes
from Clase_Menu import Menu
if __name__=='__main__':
    Clientes = Lista_de_Clientes()
    Clientes.cargadatos()
    Reparaciones = Lista_de_Reparaciones()
    Reparaciones.cargadatos()
    menu = Menu()
    menu.run(Clientes,Reparaciones)
