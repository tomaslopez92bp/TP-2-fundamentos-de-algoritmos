import sys #importamos sys para poder ingresar datos por consola
from dependencia_judicial import DependenciaJudicial #importamos la clase que creamos en el punto 1 para poder usarla

f = open(sys.argv[1],"r", encoding = "latin-1")
lat = float(sys.argv[2])
lng = float(sys.argv[3])

distanciaMinima = 20015 #máxima distancia posible entre dos puntos en la tierra.
dependenciaCercana = None
for linea in f:
    if "Fuero" in linea: #desestimamos el título
        continue
    valores = linea.split(";")
    index = valores[0]
    fuero = valores[1]
    nombre = valores[2]
    tipo = valores[3]
    direccion = valores[4]
    localidad = valores[5]
    departamento = valores[6]
    telefono = valores[7]
    latitud = valores[8].replace(",", ".") #si el valor trae una coma, reemplazarlo por punto.
    longitud = valores[9].replace(",", ".") #si el valor trae una coma, reemplazarlo por punto.
    dependencia = DependenciaJudicial(index, fuero, nombre, tipo, direccion, localidad,\
                                      departamento, telefono, latitud, longitud)
    distancia = dependencia.distancia(lat, lng)
    if distancia < distanciaMinima:
        distanciaMinima = distancia
        dependenciaCercana = dependencia
        
f.close() #cerramos el archivo

print(dependenciaCercana) #imprimos por pantalla la dependencia mas cercana a esos puntos.
    




