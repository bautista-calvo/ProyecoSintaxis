#TadMedicamento

def crearMed():
    #Crea un medicamento vacio
    med=[0,"","","","",0,0,0]
    return med

def cargarMed(med,codmed,nommed,droga,obrasoc,plan,importe,fecha,hora):
    #Carga el medicamento vacio
    #[codigo medicamento, nombre medicamento, droga, obra social, plan, importe, fecha, hora de venta]
    med[0]=codmed
    med[1]=nommed
    med[2]=droga
    med[3]=obrasoc
    med[4]=plan
    med[5]=importe
    med[6]=fecha
    med[7]=hora
    
def verCodigo(med):
    #Retorna el codigo del medicamento
    return med[0]

def verNombre(med):
    #Retorna el nombre del medicamento
    return med[1]

def verDroga(med):
    #Retorna el nombre de la droga
    return med[2]

def verObra(med):
    #Retorna la obra social
    return med[3]

def verPlan(med):
    #Retorna el plan
    return med[4]

def verImporte(med):
    #Retorna el importe
    return med[5]

def verFecha(med):
    #Retorna la fecha
    return med[6]

def verHora(med):
    #Retorna la hora
    return med[7]

def modCodigo(med,codmed):
    #Modifica el codigo del medicamento
    med[0]=codmed

def modNombre(med,nommed):
    #Modifica el nombre del medicamento
    med[1]=nommed

def modDroga(med,droga):
    #Modifica el nombre de la droga
    med[2]=droga

def modObra(med,obrasoc):
    #Modifica la obra social
    med[3]=obrasoc

def modPlan(med,plan):
    #Modifica el plan
    med[4]=plan

def modImporte(med,importe):
    #Modifica el importe
    med[5]=importe

def modFecha(med,fecha):
    #Modifica la fecha
    med[6]=fecha

def modHora(med,hora):
    #Modifica la hora
    med[7]=hora
    
def asignarMed(med1,med2):
    #Asigna los datos de un medicamento en otro
    modCodigo(med1, verCodigo(med2))
    modNombre(med1, verNombre(med2))
    modDroga(med1, verDroga(med2))
    modObra(med1, verObra(med2))
    modPlan(med1, verPlan(med2))
    modImporte(med1, verImporte(med2))
    modFecha(med1, verFecha(med2))
    modHora(med1, verHora(med2))