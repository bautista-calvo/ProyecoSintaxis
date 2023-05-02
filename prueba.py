import datetime
from TadFarmacia import *
from TadMedicamento import *

# ano=int(input("Ingrese el año: "))
# mes=int(input("Ingrese el mes: "))
# dia=int(input("Ingrese el dia: "))
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

# fecha=datetime.datetime.now()
# hora=datetime.datetime.strftime(fecha, "%H")

# print(fecha)
# print(hora)

farmacia=input("Ingrese el nombre de la farmacia: ")
farmacia=crearFarmacia()




cargarYListarMed()
cargarYListarMed()
cargarYListarMed()

plandet=input("Ingrese el plan al que desea agregarle un 20 porciento de descuento: ")
for medi in farmacia:
    if medi[4]==plandet:
        medi[5]=medi[5]*0.8
    print(medi[5])