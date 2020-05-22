# Definicion del tipo DependenciaJudicial.
class DependenciaJudicial:
    
    def __init__(self,index,fuero,nombre,tipo,direccion,localidad,departamento,telefono,latitud,longitud):
        self._index = int(index)
        self._fuero = fuero
        self._nombre = nombre
        self._tipo = tipo
        self._direccion = direccion
        self._localidad = localidad
        self._departamento = departamento
        self._telefono = telefono
        self._latitud = latitud
        self._longitud = longitud
    
    #definimos las funciones que acceden a la representacion anterior 
    #no queremos acceder a las vbles usando el _ (guion bajo) por ser un valor privado    
    
    def fuero(self):
        return self._fuero
    
    def nombre(self):
        return self._nombre
    
    def tipo_de_ente(self):
        return self._tipo
    
    def direccion(self):
        return self._direccion
    
    def locatidad(self):
        return self._localidad
    
    def departamento_judicial(self):
        return self._departamento
    
    def telefono(self):
        return self._telefono
    
    def latitud(self):
        return self._latitud
    
    def longuitud(self):
        return self._longitud
    
    def distancia(self, lat, lng):
        return float(((float(self._latitud)-float(lat))**2 + (float(self._longitud)-float(lng))**2)**0.5)
    
    #creamos las operaciones para comparar dos dependencias judiciales
    # denifimos los operadores "menor" y "igualdad"
    
    def __lt__(self,other):
        return (self.departamento_judicial() < other.departamento_judicial()) or\
               (self.departamento_judicial() == other.departamento_judicial() and self.fuero() < other.fuero()) or \
               (self.departamento_judicial() == other.departamento_judicial() and self.fuero() == other.fuero() and
                self.nombre () < other.nombre())
    
    def __eq__(self,other):
        return self.departamento_judicial() == other.departamento_judicial() and \
               self.fuero() == other.fuero() and \
               self.nombre() == other.nombre()
               
    # Estructura de representación: {fuero;nombre;direccion;localidad}             
    def __repr__(self):
        return "{" + self._fuero + ";" + self._nombre + ";" + \
            self._direccion + ";" + self._localidad + "}"
    
#algunas pruebas simples    
#depjud1 = DependenciaJudicial("x,f,n,tipo,dir,local,dpto,tel,lat,lng")
#depjud2 = DependenciaJudicial("x,f,n,tipo,dir,local,dpto,tel,lat,lng")
#depjud3 = DependenciaJudicial("x1,f,z,tipo,dir,local,dpto,tel,lat,lng")
#print(depjud1.fuero())
    #anda OK
#print(depjud1.direccion())
    #anda OK
    
    #probamos imprimir el depjud definido de ejemplo completo
#print (depjud1) #nunca le indicamos como tiene que imprimirlo, nos muestra solo su ubicación.
#definimos como queremos que se muestre. ->  {fuero;nombre;direccion;localidad}
#lo agregamos dentro de Class para ver si funcione. Funciona OK!

#probamos las funciones "menor" e "igualdad"
#print(depjud1==depjud2) #nos devuelve TRUE! Funciona bien
#print(depjud1==depjud3) #nos devuelve FALE! Funciona bien
#print(depjud1 < depjud3) #nos devuelve TRUE! Funciona bien a<z
#print(depjud3 < depjud2) #nos devuelve FALE! Funciona bien
