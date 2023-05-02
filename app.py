import datetime
from TadFarmacia import *
from TadMedicamento import *



#Funciones
def seleccionMenu():
    print("Ingrese A si quiere agregar venta de medicamento")
    print("Ingrese B si quiere modificar venta de medicamento por nombre")
    print("Ingrese C si quiere eliminar venta de medicamento por código")
    print("Ingrese D si quiere ver el listado de medicamentos")
    print("Ingrese E si quiere generar un informe indicando el monto recaudado por cada obra social")
    print("Ingrese F si quiere modificar importe con un 20 porciento de descuento a medicamentos de un plan determinado")
    print("Ingrese G si quiere eliminar todas las ventas del último mes de los medicamentos que contengan una droga dada")
    print("Ingrese H si quiere generar una cola con nombre, droga y fecha de los medicamentos que fueron vendidos por una determinada obra social.")
    print("Ingrese I si dada una hora, quiere listar la cantidad/monto de medicamentos vendidos ese día hasta la hora indicada")
    a = input("Seleccion: ")
    return a

def cargarYListarMed():
    med=crearMed()
    codmed=int(input("Ingrese el codigo del medicamento: "))
    nommed=input("Ingrese el nombre del medicamento: ")
    droga=input("Ingrese la droga: ")
    obra=input("Ingrese la obra social: ")
    plan=input("Ingrese el plan: ")
    importe=int(input("Ingrese el importe: "))
    fecha=datetime.datetime.now()
    hora=datetime.datetime.strftime(fecha, "%H")
    cargarMed(med,codmed,nommed,droga,obra,plan,importe,fecha,hora)
    farmacia.append(med)


def modificarMed(busqueda):
    cod=int(input("Ingrese el nuevo codigo: "))
    droga=input("Ingrese la nueva droga: ")
    obrasoc=input("Ingrese la nueva obra social: ")
    plan=input("Ingrese el nuevo plan: ")
    importe=int(input("Ingrese el nuevo importe: "))
    modCodigo(busqueda, cod)
    modDroga(busqueda, droga)
    modObra(busqueda, obrasoc)
    modPlan(busqueda, plan)
    modImporte(busqueda, importe)
    




#MAIN 

farmacia=input("Ingrese el nombre de la farmacia: ")
farmacia=crearFarmacia()
x=1

while x==1:
    choise = seleccionMenu()
    if choise == "A":
        cargarYListarMed()
    elif choise == "B":
        nombre=input("Ingrese el nombre a buscar: ")
        for medi in farmacia:
            if medi[1]==nombre:
                modificarMed(nombre)
                print("Cambio hecho exitosamente")
                return True
        print("No se encontro una venta de medicamento con ese nombre")
        return False
    elif choise == "C":
        codigo=int(input("Ingrese el codigo a eliminar: "))
        for medi in farmacia:
            if medi[0]==codigo:
                farmacia.remove(medi)
                print("Eliminado exitosamente")
                return True
        print("No se encontro una venta de medicamento con ese codigo")
        return False
    elif choise == "D":
        for medi in farmacia:
            print(medi)
    elif choise == "E":
        monto={}
        for medi in farmacia:
            if medi[3] in monto:
                monto[medi[3]]+=medi[5]
            else:
                monto[medi[3]]=medi[5]
        print(monto)
    elif choise == "F":
        plandet=input("Ingrese el plan al que desea agregarle un 20 porciento de descuento: ")
        for medi in farmacia:
            if medi[4]==plandet:
                medi[5]=medi[5]*0.8
    elif choise == "G":
        