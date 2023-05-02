#TadFarmacia

def crearFarmacia():
    #Crea una farmacia vacia
    farmacia=[]
    return farmacia

def agregarMed(farmacia,p):
    #Agrega un medicamento
    farmacia.append(p)

def eliminarMed(farmacia,p):
    #Elimina un medicamento
    farmacia.remove(p)

def recuperarMed(farmacia,i):
    #retorna un medicamento de la posicion enesima
    return farmacia[i-1]

def tamanio(farmacia):
    #retorna la cantidad de medicamentos del super
    return len(farmacia)

def existe(farmacia):
    #retorna un booleano indicando si existe la farmacia
    if farmacia:
        return true
    else:
        return false
    
